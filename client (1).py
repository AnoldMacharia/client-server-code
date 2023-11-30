import socket

# Step 1: Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print(f"Connected to {server_address}")

# Step 3: Send data to the server
message_to_send = "Hello, server! This is the client."
client_socket.send(message_to_send.encode('utf-8'))

# Step 4: Receive data from the server
data = client_socket.recv(1024)
print(f"Received data: {data.decode('utf-8')}")

# Step 5: Close the connection
client_socket.close()
