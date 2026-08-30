import socket
import pickle


# Define DataObject class
class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values


HOST = '127.0.0.1'
PORT = 5001

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to host and port
server.bind((HOST, PORT))

# Listen for client connections
server.listen(1)

print("Server waiting for connection...")

# Accept client connection
conn, addr = server.accept()
print("Connected by:", addr)

# Receive serialized object
data = conn.recv(4096)

# Deserialize object
obj = pickle.loads(data)

# Display object details
print("Name:", obj.name)
print("Values:", obj.values)

# Calculate sum
total = sum(obj.values)

# Create response
response = f"Hello {obj.name}, Sum of values = {total}"

# Serialize and send response
conn.send(pickle.dumps(response))

# Close connections
conn.close()
server.close()
