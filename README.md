# ChatTCP - Real-Time Chat with TCP Sockets

This project presents a real-time chat application using Python and TCP sockets, built as a practical exercise in socket programming for a Computer Networks class.

The repository implements a multi-client server-client architecture where a central server accepts simultaneous connections, manages connected users, and broadcasts messages across all active sessions.

## Objective

The project's objective is to implement socket-based communication between multiple processes running on the same machine or across a local network, demonstrating the fundamentals of TCP connection handling, concurrent client management with threads, and real-time message broadcasting.

## Features

- TCP server accepting multiple simultaneous clients;
- thread-per-client model for concurrent message handling;
- username registration on connection handshake;
- broadcast of messages to all connected users except the sender;
- automatic notification on user join and disconnect;
- graceful error handling on abrupt client disconnection.

## Project Structure

```
├── server.py
├── client.py
├── config.py
├── documentacao.pdf
└── README.md
```

## Technologies

- Python
- socket
- threading
- config.py for centralized HOST and PORT settings

## How to run locally

### Clone the repository:

```
git clone https://github.com/leomsfreitas/SocketTCP
```

### No installation required:

All libraries used (`socket` and `threading`) are part of the Python standard library. Python 3.x is the only prerequisite.

### Start the server:

```
python server.py
```

The server will start listening on `0.0.0.0:2026`. Keep this terminal open for the duration of the session.

### Connect a client:

Open a new terminal for each participant and run:

```
python client.py
```

Enter a username when prompted. The connection will be established and all other connected users will be notified.

## How to use

After connecting, type any message and press Enter to broadcast it to all other participants. Messages are displayed in the format `username: message`.

To disconnect, press `Ctrl+C` in the client terminal. The server will automatically notify the remaining participants.

## Network configuration

By default, the client connects to `127.0.0.1` (localhost). To connect clients across different machines on the same network, update the `HOST` variable in `client.py` to the server machine's local IP address:

```python
HOST = "192.168.1.10"
```

The server already listens on `0.0.0.0`, accepting connections from any available network interface.
