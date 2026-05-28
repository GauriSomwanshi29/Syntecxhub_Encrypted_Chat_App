# 🔐 Syntecxhub Encrypted Chat App

A secure client-server chat application built using **Python**, **TCP sockets**, and **AES encryption**.
This project demonstrates how messages can be encrypted before sending and decrypted safely after receiving.

---

## 📌 Project Overview

The **Encrypted Chat App** is a cybersecurity-based project created as part of the **Syntecxhub Internship Program**.

The main purpose of this project is to show how secure communication works between a client and a server.
Every message typed by the user is encrypted using AES before it is sent through the network.

---

## 🚀 Features

* 🔐 AES-based message encryption
* 🌐 TCP socket communication
* 🖥️ Client-server architecture
* 👥 Multiple client support using threading
* 📝 Message logging system
* 🔑 Pre-shared secret key handling
* 🧩 Safe nonce/IV usage for encryption
* ⚠️ Basic error handling for client disconnects

---

## 🛠️ Technologies Used

* Python
* Socket Programming
* Threading
* PyCryptodome
* AES Encryption

---

## 📂 Folder Structure

```bash
Syntecxhub_Encrypted_Chat_App/
│
├── server.py
├── client.py
├── crypto_utils.py
├── chat_log.txt
└── README.md
```

---

## ⚙️ Installation

First, install the required Python library:

```bash
pip install pycryptodome
```

---

## ▶️ How to Run

### 1️⃣ Start the Server

```bash
python server.py
```

### 2️⃣ Start the Client

Open another terminal and run:

```bash
python client.py
```

### 3️⃣ Send Messages

Type your message in the client terminal.
The message will be encrypted before sending and decrypted on the server side.

---

## 🔐 How Encryption Works

1. User enters a message.
2. The message is encrypted using AES.
3. The encrypted text is sent to the server.
4. Server receives the encrypted message.
5. Server decrypts it and displays the original message.
6. Message is stored in the log file.

---

## 📸 Output Preview

```bash
Client Side:
You: Hello Syntecxhub
Encrypted message sent: kdj38sjd92ks...

Server Side:
Client: Hello Syntecxhub
```

---

## 📚 Learning Outcomes

Through this project, I learned:

* How socket communication works
* How AES encryption protects messages
* How client-server applications are created
* How multiple clients can connect using threading
* Why secure key handling is important in cybersecurity

---

## 🔮 Future Improvements

* Add GUI using Tkinter
* Add username support
* Add timestamp for each message
* Add encrypted message history
* Add authentication system
* Add better key exchange method

---

## 👩‍💻 Developed By

**Gauri Somwanshi**
Cyber Security Intern
Syntecxhub Internship Program

---

## 📢 Internship Task

This project was developed as part of the **Week 2 Cyber Security Internship Task** assigned by **Syntecxhub**.

---

## ⭐ Conclusion

This project shows a basic but effective implementation of secure chat communication using encryption.
It is useful for understanding the foundation of secure messaging systems and network security.
