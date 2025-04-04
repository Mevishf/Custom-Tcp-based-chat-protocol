import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5088

# Receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

# Send messages to the server
def send_messages():
    while True:
        try:
            message = input("")
            client.send(message.encode('utf-8'))
        except:
            print("Disconnected from server.")
            client.close()
            break

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Enter a username
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
