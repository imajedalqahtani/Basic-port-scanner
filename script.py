import socket 
from datetime import datetime

# function to scan a range of ports on a target machine
def scan_ports(target, start_port, end_port):

    print(f"\nScanning target: {target}")  
    print(f"Time started: {datetime.now()}\n")  # Show start time

    try:
        # Convert domain name into IP address
        target_ip = socket.gethostbyname(target)
        print(f"IP Address: {target_ip}\n")

    except socket.gaierror:
        # If domain name cannot be resolved
        print("Hostname could not be resolved")
        return  # Stop the function

    open_ports = []  # List to store open ports

    # Loop through each port in the given range
    for port in range(start_port, end_port + 1):

        # Create a TCP socket (IPv4 + TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout so we don't wait too long on each port
        sock.settimeout(0.5)

        # Try connecting to the port
        result = sock.connect_ex((target_ip, port))

        # If result is 0 then connection is successful then port is open
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)  # Save open port

        sock.close()  # close the connection

    print("\nScan complete.")  
    print(f"Open ports: {open_ports}")  # Show results


# Ask user for input
target = input("Enter target for example: (localhost or IP): ")
start = int(input("Start port: "))
end = int(input("End port: "))

# Run the scanner
scan_ports(target, start, end)