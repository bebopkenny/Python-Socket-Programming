# Python Socket Programming 🚀

This repository contains a simple client-server application built in Python using sockets and threading. The **server** listens for incoming TCP connections on a specified port, and the **client** can connect to it to send and receive messages.

---

## Features ⚙️

- **Multi-threaded Server**: Each new client connection is handled in a separate thread, allowing multiple simultaneous connections.
- **Message Size Protocol**: The client sends a fixed-size header (64 bytes) indicating the size of the message that follows.
- **Graceful Disconnection**: A special `!DISCONNECT` message cleanly closes the connection on both client and server.

---

## Getting Started 🎉

### Prerequisites

- Python 3.x installed
- Basic understanding of TCP/IP networking

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
2. Navigate into the cloned folder:
   ```bash
   cd Python-Socket-Programming

## Usage
1. Start the server:
   ```bash
   python3 server.py
- The server will display [STARTING] server is starting... and then [LISTENING] Server is listening <IP_ADDRESS>.
2. Run the Client:
  ```bash
  python3 client.py
  ```
- The client will connect to the server, send a "Hello World!" message, then wait for user input.
- Press Enter to send more messages or eventually disconnect with !DISCONNECT.
You can edit PORT and SERVER in both files if you need a different port or IP address.

---

## Contributing 🤝
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or add.

---

## License
Feel free to use this project under the MIT License.
