import socket
import json
from math import gcd
import os


def register_key():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    for d in range(2, phi):
        if (d * e) % phi == 1:
            break
    public_key = (e, n)
    private_key = (d, n)
    print(f"Public Key: {public_key}\nPrivate Key: {private_key}")
    return public_key, private_key


def caesar_encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def register_with_server(username, public_key, host="localhost", port=5001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(
        json.dumps(
            {"action": "register", "username": username, "public_key": public_key}
        ).encode()
    )
    response = json.loads(s.recv(4096).decode())
    s.close()
    return response


def get_receiver_public_key(target_user, host="localhost", port=5001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(json.dumps({"action": "get_key", "target_user": target_user}).encode())
    response = json.loads(s.recv(4096).decode())
    s.close()
    if response["status"] == "ok":
        return tuple(response["public_key"])
    else:
        print("Error retrieving public key:", response.get("message"))
        return None


def send_file(
    filename, key, receiver_e, receiver_n, receiver_host="localhost", receiver_port=6000
):
    # Encrypt key using receiver's public key
    encrypted_key = pow(key, receiver_e, receiver_n)
    # Read and encrypt file contents
    with open(filename, "r") as f:
        message = f.read()
    encrypted_message = caesar_encrypt(message, key)
    # Connect and send to receiver
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((receiver_host, receiver_port))
    # Send encrypted key and filename meta first
    payload = {"encrypted_key": encrypted_key, "filename": os.path.basename(filename)}
    s.send(json.dumps(payload).encode())
    ack = s.recv(1024)  # Wait for receiver to get ready
    # Send file contents (encrypted)
    s.sendall(encrypted_message.encode())
    s.close()
    print(f"Encrypted Key sent: {encrypted_key}\nEncrypted file sent.")


def menu(username, public_key, receiver_username):
    receiver_pub = get_receiver_public_key(receiver_username)
    if not receiver_pub:
        print("Cannot proceed without receiver's public key.")
        return
    receiver_e, receiver_n = receiver_pub
    while True:
        print("\n===== Server Menu =====")
        print("1. Send Data (send file)")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            filename = input("Enter path to txt file to send: ")
            if not os.path.exists(filename):
                print("File not found.")
                continue
            key = int(input("Enter the key (0-25) for Caesar encryption: "))
            send_file(filename, key, receiver_e, receiver_n)
        elif choice == "2":
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    username = input("Enter your username: ")
    receiver_username = input("Enter receiver's username: ")
    public_key, private_key = register_key()
    register_with_server(username, public_key)
    menu(username, public_key, receiver_username)
