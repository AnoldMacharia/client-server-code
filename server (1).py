import socket

# Step 1: Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Step 3: Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {server_address}")

# Step 4: Define allowed and blocked IP addresses
allowed_ip_addresses = ['127.0.0.1']  # Add the IP addresses you want to allow
blocked_ip_addresses = []

# Step 5: Accept a connection and check firewall
while True:
    client_socket, client_address = server_socket.accept()
    if client_address[0] in allowed_ip_addresses and client_address[0] not in blocked_ip_addresses:
        print(f"Accepted connection from {client_address}")
        break
    else:
        print(f"Connection from {client_address} blocked by firewall.")
        client_socket.close()

# Step 6: Receive and send data
data = client_socket.recv(1024)
print(f"Received data: {data.decode('utf-8')}")

message_to_send = "Hello, client! This is the server."
client_socket.send(message_to_send.encode('utf-8'))

# Step 7: Close the connection
client_socket.close()
server_socket.close()
