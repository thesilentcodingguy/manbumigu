import socket
import pickle


# Define DataObject class
class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values


HOST = '127.0.0.1'
PORT = 5001

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Get input from user
name = input("Enter name: ")

values = list(
    map(
        int,
        input("Enter numbers separated by space: ").split()
    )
)

# Create DataObject
obj = DataObject(name, values)

# Serialize and send object
client.send(pickle.dumps(obj))

# Receive and deserialize response
response = pickle.loads(client.recv(4096))

# Display response
print("Server Response:", response)

# Close client socket
client.close()
