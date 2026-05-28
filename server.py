import socket
import threading
from crypto_utils import decrypt_message

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("Server started...")
print("Waiting for clients...")

def handle_client(client):
    while True:
        try:
            encrypted_message = client.recv(1024).decode()

            if not encrypted_message:
                break

            decrypted_message = decrypt_message(encrypted_message)

            print("Client:", decrypted_message)

            with open("chat_log.txt", "a") as file:
                file.write("Client: " + decrypted_message + "\n")

        except:
            print("Client disconnected.")
            clients.remove(client)
            client.close()
            break

while True:
    client, address = server.accept()
    print("Connected with:", address)

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()