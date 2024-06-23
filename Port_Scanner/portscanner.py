import socket
import threading

def scan(target, ports):
    for port in range(1, ports + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass

if __name__ == "__main__":
    target = input("Enter the IP address of the target: ")
    ports = int(input("Enter the range of ports to scan: "))
    scan(target, ports)
