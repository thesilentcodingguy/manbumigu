import socket
import threading

HOST = '127.0.0.1'
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

print("Server is running...")
print("Waiting for clients to connect...")


# Broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handle messages from a client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)

            client.close()

            nickname = nicknames[index]
            nicknames.remove(nickname)

            broadcast(f"{nickname} left the chat.".encode())

            print(f"{nickname} disconnected.")
            break


# Accept new clients
def receive():
    while True:
        client, address = server.accept()

        print(f"Connected with {address}")

        client.send("NICK".encode())

        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")

        broadcast(f"{nickname} joined the chat.".encode())

        client.send("Connected to the server.".encode())

        thread = threading.Thread(
            target=handle,
            args=(client,)
        )

        thread.start()


receive()
