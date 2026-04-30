# SocketBasedChat

## Overview

SocketBasedChat is a Python-based terminal chat application that uses TCP sockets to support real-time communication between multiple clients through a centralized server. Built for networking and systems practice, this project demonstrates core concepts such as socket programming, client-server architecture, custom protocol design, concurrency with threads, and command parsing.

Users can connect to the server, choose unique usernames, send public messages, direct message specific users, rename themselves during a session, and view currently connected users.

---

## Features

### Core Functionality
- Multi-client chat server using TCP sockets
- Real-time public messaging
- Direct messaging (`/dm`)
- Active user list (`/list`)
- Username uniqueness enforcement
- Rename command (`/rename`)
- Graceful disconnect (`/quit`)
- Custom message protocol for structured communication
- Threaded server handling for multiple simultaneous clients

### Networking Concepts Demonstrated
- TCP client-server communication
- Socket lifecycle management
- Concurrent connection handling with threading
- Custom protocol serialization/deserialization
- Error handling for invalid usernames and disconnects

---

## Repository Structure

```bash
SocketBasedChat/
│── client.py           # Client-side terminal application
│── server.py           # Multi-client chat server
│── chat_protocol.py    # Shared protocol/message definitions
│── protocol.md         # Detailed custom protocol specification
│── README.md           # Project documentation
```

---

## Installation & Requirements

### Prerequisites
- Python 3.10+
- No external libraries required (uses built-in `socket`, `threading`, and `json`/string parsing)

### Clone the Repository

```bash
git clone https://github.com/LouisJimenezHernandez/SocketBasedChat.git
cd SocketBasedChat
```

---

## Running the Application

### Start the Server

```bash
python server.py
```

Expected output:

```bash
[STARTED] Chat server running on host:port
```

### Start a Client (new terminal for each client)

```bash
python client.py
```

---

## Client Commands

| Command | Description |
|--------|-------------|
| `/dm username message` | Send a private message |
| `/list` | View connected users |
| `/rename new_username` | Change your username |
| `/quit` | Disconnect from server |
| `message text` | Send public chat message |

---

## Example Session

### Client A

```bash
Enter username: louis
[OK] Welcome, louis
Hello everyone!
```

### Client B

```bash
Enter username: lily
[OK] Welcome, lily
/dm louis Hey there!
```

### Server Behavior
- Broadcasts public messages to all connected users
- Routes DMs only to specified recipients
- Rejects duplicate usernames
- Updates server records on rename

---

## Protocol Design

The application uses a lightweight custom protocol defined in `chat_protocol.py` and documented in `protocol.md`.

### Example Message Types
- `JOIN`
- `MSG`
- `DM`
- `LIST`
- `RENAME`
- `QUIT`
- `ERROR`
- `OK`

### Example Serialized Message

```txt
MSG|louis|Hello world!
```

This structured format ensures predictable parsing and extensibility for future commands.

---

## Educational Value

This project was designed to strengthen understanding of:

- Socket programming fundamentals
- Application-layer protocol design
- Client-server architectures
- Thread synchronization
- Command parsing
- Error handling in distributed systems

---

## Future Improvements

Potential extensions include:

- Group chat rooms
- Persistent chat history
- File transfer support
- Emoji/reaction commands
- Authentication/password system
- GUI client interface
- End-to-end encryption

---

## Common Issues

### Username Already Taken
```bash
[ERROR] Username already taken
```
Choose a unique username.

### Windows Socket Error (`WinError 10038`)
This typically occurs when the client attempts to send after the socket has already been closed. Ensure the client exits immediately after failed login attempts.

---

## Resume-Style Project Description

**SocketBasedChat — Python Networking Project**  
- Developed a multi-client terminal chat application in Python using TCP sockets and multithreading for real-time communication  
- Designed and implemented a custom application-layer messaging protocol supporting public chat, direct messaging, user listing, and dynamic username changes  
- Built concurrent server-side connection management with username validation, command parsing, and graceful session handling

---

## License

This project is intended for educational use and coursework purposes.

---

## Author

**Louis Jimenez-Hernandez**  
Boston University — Engineering / Computer Science  
GitHub: https://github.com/LouisJimenezHernandez