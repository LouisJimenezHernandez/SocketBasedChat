# client.py

import socket
import threading
from chat_protocol import *

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client):
    while True:
        try:
            raw = client.recv(1024).decode()

            if not raw:
                print("Disconnected from server.")
                break

            command, parts = parse_message(raw)

            if command == OK:
                print(f"[OK] {parts[0]}")

            elif command == ERROR:
                print(f"[ERROR] {parts[0]}")

                if "Username" in parts[0]:
                    print("Closing client...")
                    client.close()
                    break

            elif command == SERVER:
                print(f"[Server] {parts[0]}")

            elif command == FROM:
                sender = parts[0]
                message = parts[1]
                print(f"{sender}: {message}")

            elif command == PRIVATE:
                sender = parts[0]
                message = parts[1]
                print(f"[DM from {sender}] {message}")

            elif command == USERLIST:
                print(f"Online users: {parts[0]}")

            else:
                print(raw)

        except:
            break


def main():
    username = input("Enter username: ").strip()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(build_message(JOIN, username).encode())

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )
    receive_thread.start()

    print("For a list of commands, type /help")

    while True:
        text = input().strip()

        if text == "/quit":
            client.sendall(build_message(QUIT).encode())
            break

        elif text == "/list":
            client.sendall(build_message(LIST).encode())

        elif text == "/help":
                print("Commands:")
                print("/dm username message")
                print("/list")
                print("/whoami")
                print("/quit")

        elif text == "/whoami":
            client.sendall(build_message(WHOAMI).encode())

        elif text.startswith("/dm "):
            pieces = text.split(" ", 2)

            if len(pieces) < 3:
                print("Usage: /dm username message")
            else:
                recipient = pieces[1]
                message = pieces[2]
                client.sendall(build_message(DM, recipient, message).encode())

        else:
            client.sendall(build_message(MSG, text).encode())

    client.close()


if __name__ == "__main__":
    main()