import socket
import re
import time

PORT = 5555

def get_ip():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.connect(('8.8.8.8', 80))
	local_ip = sock.getsockname()
	sock.close()
	return local_ip[0]

def get_subnet():
	local_ip = get_ip()
	subnet = re.sub(r"\.(\d+)$", r".255", local_ip)
	return subnet

def broadcast(message, SUB_NET):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	try:
		sock.sendto(message, (SUB_NET, PORT))
		print(f"[SENT] {msg}")
		time.sleep(1)
	except KeyboardInterrupt:
		print("[BROADCAST STOPPED]")
	finally:
		sock.close()

def main():
	global msg
	print("\n[GITHUB] https://github.com/aluminium65")
	print(f"[IP] {get_ip()}")
	print(f"[NETWORK] {NETWORK}")
	print(f"[PORT] {PORT}\n")

	print("Enter the message to broadcast:")
	msg = input("  >> ")

	SUBNET = get_subnet()
	MESSAGE = msg.encode("UTF-8")
	broadcast(MESSAGE, SUBNET)

NETWORK = re.sub(r"\.(\d+)$", r".0/24", get_ip())


if __name__ == "__main__":
	print("""
 __   __   ___   __   __     ____  __   ___ _____
|  \\ |  ) |   | |  | |   \\  |     |  | |      |
|__/ |_/  |   | |__| |    | |     |__| |___   |
|  \\ |\\   |   | |  | |    | |     |  |     |  |
|__/ | \\  |___| |  | |___/  |____ |  |  ___|  |

-------------------------By aluminium-----------------------------


		""")
	try:
		main()
	except KeyboardInterrupt:
		print("\b\b[Exiting]")
		exit()