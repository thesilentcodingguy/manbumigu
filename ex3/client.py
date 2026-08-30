import socket
import threading

HOST = "127.0.0.1"
PORT = 5002

nickname = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))


# Receive messages from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NICK":
                client.send(nickname.encode())

            else:
                print(message)

        except:
            print("Connection closed.")
            client.close()
            break


# Send messages to server
def write():
    while True:
        message = input("")

        client.send(
            f"{nickname}: {message}".encode()
        )


# Thread for receiving messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()


# Thread for sending messages
write_thread = threading.Thread(target=write)
write_thread.start()
