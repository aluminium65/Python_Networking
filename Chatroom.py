import socket
import sys
import select


def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('8.8.8.8', 80))
    local_ip = sock.getsockname()
    sock.close()
    return local_ip[0]


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((IP, PORT))
    server.listen()
    print(f"[*] Listening on {IP}:{PORT}")
    print("[*] Press Ctrl + C to exit.")
    socket_list = [server]

    try:
        while True:
            read_list, _, _ = select.select(socket_list, [], [])
            for notification in read_list:
                if notification == server:
                    connection, address = server.accept()
                    socket_list.append(connection)
                    CLIENTS[connection] = address[0]
                    print(f"[{address[0]}] CONNECTED")
                else:
                    client_ip = CLIENTS[notification]
                    message = notification.recv(1024)
                    if message.decode() == "not_available_ever_xxxx":
                        msg = f"[{client_ip}] DISCONNECTED"
                        print(msg)
                        socket_list.remove(notification)
                        del CLIENTS[notification]
                        continue
                    if message:
                        msg = f"[{client_ip}] {message.decode().replace("\n", "")}"
                        print(msg)
                        broadcast(CLIENTS, notification, msg)

    except KeyboardInterrupt:
        print("\b\b[*] Exiting!")
        server.close()
        sys.exit()


def broadcast(clients, notified_socket, message):
	for client_socket in clients:
		if client_socket != notified_socket:
			client_socket.send(message.encode("UTF-8"))


def main_client():
    print("[*] Enter the IP address of the Chatroom:")
    target_ip = input(" > ")
    print("\n[*] Enter the Port Number:")
    try:
        target_port = input(" > ")
        target_port = int(target_port)
    except ValueError:
        print("\nThe Value must be numeric.(1 to 65536)")
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((target_ip, target_port))
        client_sock.setblocking(False)
        print(f"[CHATROOM] CONNECTED")
    except:
        print("[*] Unable to connect!")
        sys.exit()

    with client_sock as sock:
        while True:
            try:
                read_list, _, _ = select.select([sock, sys.stdin], [], [])
                for src in read_list:
                    if src == sock:
                        try:
                            message = sock.recv(1024)
                            if message:
                                print(message.decode())
                        except BlockingIOError:
                            pass
                    elif src == sys.stdin:
                        message = sys.stdin.readline().rstrip("\n")
                        if message:
                            sock.send(message.encode())
            except KeyboardInterrupt:
                sock.send(b"not_available_ever_xxxx")
                print("[CHATROOM] DISCONNECTED")
                sys.exit()
                break



if __name__== "__main__":
    print("""
  [][][] []  []  [][]  [][][][] [][]    [][][]   [][][]  [][]  [][]
[]       []  [] []  []    []    []  [] []    [] []    [] [] [][] []
[]       [][][] [][][]    []    [][]   []    [] []    [] []  []  []
[]       []  [] []  []    []    [] []  []    [] []    [] []      []
  [][][] []  [] []  []    []    []  []  [][][]   [][][]  []      []

 -------------------------By aluminium----------------------------
        """)

    while True:
        print("[*] Select the appropriate option:\n")
        print("1, Host a Chatroom.")
        print("2, Join a Chatroom.\n")
        try:
            option = input(" > ")
            option = int(option)
            break
        except ValueError:
            print("[*] Invalid option.")

    if option == 1:
        IP = get_ip()
        PORT = 9091
        CLIENTS = {}

        main()

    if option == 2:
        client_sock = main_client()
        client_communication(client_sock)

    else:
        print("[*] Invalid Option!")