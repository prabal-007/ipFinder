import socket
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
print(f"Host name = {hostname}")
print(f'IP address = {host}')