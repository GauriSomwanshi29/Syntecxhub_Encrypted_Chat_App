import socket
from crypto_utils import encrypt_message

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server.")
print("Type your message below.")
print("Type 'exit' to stop.")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Chat closed.")
        break

    encrypted_message = encrypt_message(message)

    print("Encrypted message sent:", encrypted_message)

    client.send(encrypted_message.encode())

client.close()