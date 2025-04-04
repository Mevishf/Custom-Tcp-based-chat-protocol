import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5088
clients = {}  # Map client sockets to usernames or addresses

# Broadcast messages to all clients except the sender
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                del clients[client]

# Handle individual client communication
def handle_client(client_socket):
    try:
        # Receive the client's username
        username = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = username  # Map the socket to the username
        print(f"{username} has joined the chat!")

        # Notify others about the new client
        broadcast(f"{username} has joined the chat!".encode('utf-8'), client_socket)

        while True:
            # Receive messages from the client
            message = client_socket.recv(1024)
            if message:
                tagged_message = f"{clients[client_socket]}: {message.decode('utf-8')}"
                print(tagged_message)
                broadcast(tagged_message.encode('utf-8'), client_socket)
    except:
        print(f"{clients[client_socket]} has disconnected.")
        broadcast(f"{clients[client_socket]} has left the chat.".encode('utf-8'), client_socket)
        del clients[client_socket]
        client_socket.close()

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connected with {str(client_address)}")

        # Start a thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server()
