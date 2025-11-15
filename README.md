# 🐍 Python Intermediate Networking Projects

A collection of Python projects demonstrating **intermediate networking** and **concurrency** principles. This repository focuses on building robust applications that manage simultaneous connections and utilize advanced socket programming techniques.

---

## 🎯 Projects in This Repository

These projects move beyond simple one-to-one communication, requiring knowledge of non-blocking I/O and architectural design patterns.

| Project Name | Key Concepts Demonstrated | Description |
| :--- | :--- | :--- |
| **Multi-Client Chatroom (`Chatroom.py`, `broadcast_message.py`)** | I/O Multiplexing (`select`), Concurrency, Socket Programming, Error Handling. | A TCP server and client implementation that allows multiple clients to connect simultaneously and broadcast messages to all other active users. |
| **Network Utility Tool (`domain_info.py`)** | Advanced Socket Functions, Protocol Interaction, External API/Tool Integration. | A script designed to gather detailed network information, such as DNS or WHOIS data, for a given domain. |

---

## 🚀 Getting Started

### Prerequisites

To run these projects, you will need **Python 3.x**. No external libraries are typically required, as these projects primarily utilize Python's built-in `socket` and `select` modules.

### Running the Projects

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Python_Intermediate_Networking.git](https://github.com/YourUsername/Python_Intermediate_Networking.git)
    cd Python_Intermediate_Networking
    ```

2.  **To run the Chatroom:**
    * Start the server in one terminal:
        ```bash
        python Chatroom.py
        ```
    * Connect with multiple clients in separate terminals:
        ```bash
        python Client.py 
        # (Assuming you also create a simple Client.py file for connecting)
        ```

---

## 💡 Why These Projects Are Intermediate

These projects are classified as intermediate because they require:
* **Non-Blocking I/O:** Using modules like `select` to handle many clients efficiently without freezing the server process.
* **Architectural Design:** Managing lists of active sockets, handling new connections, and implementing broadcast logic.
* **Robust Error Handling:** Properly closing failed connections and managing exceptions from network operations.
