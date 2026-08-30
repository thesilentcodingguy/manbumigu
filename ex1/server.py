import socket

HOST = '127.0.0.1'
PORT = 5000

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to host and port
server.bind((HOST, PORT))

# Listen for client connections
server.listen(1)

print("Server is listening...")

# Accept client connection
conn, addr = server.accept()
print("Connected by:", addr)

# Receive data from client
data = conn.recv(1024).decode()
print("Received:", data)

# Parse numbers
numbers = list(map(int, data.split()))

# Calculate sum
result = sum(numbers)

# Send result back to client
conn.send(f"Sum = {result}".encode())

# Close connections
conn.close()
server.close()
