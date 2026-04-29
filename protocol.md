# Protocol Specification

## Overview
This application is a custom text-based application-layer protocol built on top of TCP sockets. It defines structured communication rules between clients and a centralized chat server.

All protocol messages use the following format:

COMMAND|ARG1|ARG2|MESSAGE

The pipe symbol `|` is used as the field separator.

---

# Client → Server Commands

## JOIN
Connect a user to the chat server.

Format:
JOIN|username

Example:
JOIN|Alice

---

## MSG
Send a public broadcast message to all connected users.

Format:
MSG|message

Example:
MSG|Hello everyone

---

## DM
Send a private direct message to one specific user.

Format:
DM|recipient|message

Example:
DM|Bob|Hey Bob

---

## LIST
Request a list of all active connected users.

Format:
LIST

Example:
LIST

---

## RENAME
Change your current username without disconnecting.

Format:
RENAME|new_username

Example:
RENAME|SocketQueen

---

## QUIT
Disconnect from the server cleanly.

Format:
QUIT

Example:
QUIT

---

# Server → Client Responses

## OK
Confirms successful action.

Format:
OK|message

Example:
OK|Welcome, Alice

Example:
OK|Username changed to SocketQueen

---

## ERROR
Reports invalid commands or failures.

Format:
ERROR|reason

Example:
ERROR|Username already taken

Example:
ERROR|Usage: RENAME|new_username

---

## SERVER
Broadcasts server announcements.

Format:
SERVER|message

Example:
SERVER|Alice joined the chat

Example:
SERVER|Alice is now known as SocketQueen

---

## FROM
Broadcasts a public message from another user.

Format:
FROM|sender|message

Example:
FROM|Alice|Hello everyone

---

## PRIVATE
Delivers a private direct message.

Format:
PRIVATE|sender|message

Example:
PRIVATE|Bob|Hey Alice

---

## USERLIST
Returns currently connected users.

Format:
USERLIST|user1, user2, user3

Example:
USERLIST|Alice, Bob, Charlie

---

# Design Goals
- Human-readable protocol
- Lightweight text parsing
- Expandable command system
- Structured client-server communication
- Demonstrates application-layer protocol design

---

# Networking Relevance
This application operates at the Application Layer while relying on TCP at the Transport Layer for reliable delivery. This separation mirrors real-world protocol stacks such as HTTP over TCP.

The addition of `RENAME` demonstrates dynamic session management and server-side state synchronization, where identity changes must be propagated across active network participants in real time.