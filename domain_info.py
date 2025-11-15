import socket 


common_ports_list = [
    (20, "FTP-Data", "TCP"),
    (21, "FTP-Control", "TCP"),
    (22, "SSH", "TCP"),
    (23, "Telnet", "TCP"),
    (25, "SMTP", "TCP"),
    (53, "DNS", "UDP/TCP"),
    (67, "DHCP (Server)", "UDP"),
    (68, "DHCP (Client)", "UDP"),
    (69, "TFTP", "UDP"),
    (80, "HTTP", "TCP"),
    (110, "POP3", "TCP"),
    (123, "NTP", "UDP"),
    (143, "IMAP", "TCP"),
    (161, "SNMP", "UDP"),
    (389, "LDAP", "TCP/UDP"),
    (443, "HTTPS", "TCP"),
    (445, "SMB", "TCP"),
    (587, "SMTP (Submission)", "TCP"),
    (993, "IMAPS", "TCP"),
    (995, "POP3S", "TCP"),
    (3389, "RDP", "TCP"),
    (3306, "MySQL", "TCP"),
]



def ip_finder(target_host):
	try:
		ip_addr = socket.gethostbyname(target_host)
		print(f"[+] IP Address : {ip_addr}")
	except:
		print(f"[+] Unable to find the IP Adress for {target_host}")


def reverse_dns(target_host):
	try:
		domain, x, y = socket.gethostbyaddr(target_host)
		print(f"[+] DNS : {domain}")
	except:
		print(f"[+] Unable to find the DNS for {target_host}")


def port_connect(target_host, target_port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((target_host, target_port))
	sock.close()
	return result


def port_scanner(target_host):
	for port, serv, protocol in common_ports_list:
		connection = port_connect(target_host, port)
		if connection == 0:
			print(f" --> Open port : {port}")
			print(f"     Service : {serv}")
		else:
			print(f" --> Filtered port : {port}")


def main():
	print("""

[][][]      [][][]   [][]  [][]   [][]   [][][][][] [][]    []      [][][][][] [][]    [] [][][][]   [][][]
[]    []  []      [] [] [][] [] []    []     []     [] []   []          []     [] []   [] []       []      []
[]     [] []      [] []  []  [] [][][][]     []     []  []  []          []     []  []  [] [][][]   []      []
[]    []  []      [] []      [] []    []     []     []   [] []          []     []   [] [] []       []      []
[][][]      [][][]   []      [] []    [] [][][][][] []    [][]      [][][][][] []    [][] []         [][][]

--------------------------------------------By aluminium------------------------------------------------

		""")
	print("\n[+] Enter the hostname:")
	hostname = input("  >> ")
	IP = ip_finder(hostname)
	Domain = reverse_dns(hostname)
	Ports = port_scanner(hostname)

if __name__ == "__main__":
	main()
