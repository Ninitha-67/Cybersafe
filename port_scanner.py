import socket
def scan_ports(host):
    print(f"Scanning ports on {host}...")
    open_ports = []
    for port in  range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port{port} is open")
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP or hostnames: ")
    scan_ports(target)
