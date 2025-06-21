import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.1.96", 5555))  # Make sure this is 0.0.0.0, not 127.0.0.1 or localhost
print("Listening on port 5555...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
