import socket

HOST = '127.0.0.1'
PORT = 5000

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Get numbers from user
message = input("Enter numbers separated by space: ")

# Send message to server
client.send(message.encode())

# Receive response from server
response = client.recv(1024).decode()

# Display response
print("Server Response:", response)

# Close client socket
client.close()


import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
while True:
  message = input("Send message to server: ")
  try:
    if message.lower().strip() != 'exit':
      client_socket.send(message.encode())
      data = client_socket.recv(1024).decode()
      print(f"Message received from server: {data}")
    else:
      break
  except ConnectionAbortedError as e:
    print(e)
client_socket.close()
