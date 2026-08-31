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


import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
client_socket, addr = server_socket.accept()
print(f"Connected {client_socket} on {addr}")
while True:
message = client_socket.recv(1024).decode()
try:
if not message:
print("No message received. Client may have closed the connection.")
break
if message.lower().strip() == 'exit':
print("Received 'exit' message. Closing connection.")
break
print(f"Message received from client: {message}")
list1 = message.split()
total_sum = 0
for i in list1:
total_sum += int(i)
response = client_socket.send(str(total_sum).encode())
print(f"Sending data {total_sum} to client")
except ConnectionAbortedError as e:
print(e)
client_socket.close()
server_socket.close()
