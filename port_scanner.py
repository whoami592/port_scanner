import socket
import sys
from datetime import datetime

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...\n")
    start_time = datetime.now()
    
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()
    
    end_time = datetime.now()
    print(f"\nScan completed in {end_time - start_time}")

if __name__ == "__main__":
    target = input("Enter target IP address: ")
    port_range = range(1, 1025)  # Scan common ports (1-1024)
    scan_ports(target, port_range)