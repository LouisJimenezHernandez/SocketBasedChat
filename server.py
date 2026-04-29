# server.py

import socket
import threading
from chat_protocol import *

HOST = "127.0.0.1"
PORT = 5000

clients = {}  # username -> socket
lock = threading.Lock()


def send_message(conn, command, *parts):
    message = build_message(command, *parts)
    conn.sendall(message.encode())


def broadcast(command, *parts, exclude=None):
    message = build_message(command, *parts).encode()

    with lock:
        for username, conn in clients.items():
            if conn != exclude:
                try:
                    conn.sendall(message)
                except:
                    pass


def handle_client(conn, addr):
    username = None

    try:
        # First message must be JOIN|username
        raw = conn.recv(1024).decode()
        command, parts = parse_message(raw)

        if command != JOIN or len(parts) != 1:
            send_message(conn, ERROR, "First message must be JOIN|username")
            return

        requested_username = parts[0].strip()

        with lock:
            if requested_username in clients:
                send_message(conn, ERROR, "Username already taken")
                return

            clients[requested_username] = conn
            username = requested_username

        send_message(conn, OK, f"Welcome, {username}")
        broadcast(SERVER, f"{username} joined the chat", exclude=conn)

        print(f"{username} connected from {addr}")

        while True:
            raw = conn.recv(1024).decode()
            print(f"[{username}] RAW -> {raw}")

            if not raw:
                break

            command, parts = parse_message(raw)

            if command == MSG:
                if len(parts) != 1:
                    send_message(conn, ERROR, "Usage: MSG|message")
                else:
                    broadcast(FROM, username, parts[0])

            elif command == DM:
                if len(parts) != 2:
                    send_message(conn, ERROR, "Usage: DM|recipient|message")
                else:
                    recipient = parts[0].strip()
                    message = parts[1].strip()

                    with lock:
                        target_conn = clients.get(recipient)

                    if target_conn:
                        send_message(target_conn, PRIVATE, username, message)
                        send_message(conn, OK, f"Private message sent to {recipient}")
                    else:
                        send_message(conn, ERROR, f"User {recipient} not found")

            elif command == LIST:
                with lock:
                    users = ", ".join(clients.keys())

                send_message(conn, USERLIST, users)

            elif command == QUIT:
                send_message(conn, OK, "Goodbye")
                break

            else:
                send_message(conn, ERROR, "Unknown command")

    except ConnectionResetError:
        pass

    finally:
        if username:
            with lock:
                if username in clients:
                    del clients[username]

            broadcast(SERVER, f"{username} left the chat")
            print(f"{username} disconnected")

        conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    server.settimeout(1)

    print(f"SimpleChat server running on {HOST}:{PORT}")

    try:
        while True:
            try:
                conn, addr = server.accept()

                thread = threading.Thread(
                    target=handle_client,
                    args=(conn, addr),
                    daemon=True
                )
                thread.start()

            except socket.timeout:
                continue

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        server.close()


if __name__ == "__main__":
    main()