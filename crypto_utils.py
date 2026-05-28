from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

KEY = b'1234567890123456'

def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    encrypted_data = cipher.nonce + ciphertext
    return base64.b64encode(encrypted_data).decode()

def decrypt_message(encrypted_message):
    data = base64.b64decode(encrypted_message)

    nonce = data[:16]
    ciphertext = data[16:]

    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    decrypted_message = cipher.decrypt(ciphertext).decode()

    return decrypted_message