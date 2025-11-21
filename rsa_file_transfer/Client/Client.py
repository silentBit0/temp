import socket
import threading
import json
from math import gcd
import os

public_key = None
private_key = None


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
    global public_key
    global private_key
    public_key = (e, n)
    private_key = (d, n)
    print(f"Public Key: {public_key}\nPrivate Key: {private_key}")


def caesar_decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
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


def receive_message(host="localhost", port=6000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Client listening for incoming files on {host}:{port}...")
    while True:
        conn, addr = s.accept()
        # Receive key and filename meta
        meta = conn.recv(1024)
        payload = json.loads(meta.decode())
        encrypted_key = payload["encrypted_key"]
        filename = payload["filename"]
        conn.send(b"READY")  # Acknowledge, ready for actual file
        # Receive file data
        encrypted_message = b""
        while True:
            data = conn.recv(4096)
            if not data:
                break
            encrypted_message += data
        d, n = private_key
        key = pow(encrypted_key, d, n)
        decrypted_message = caesar_decrypt(encrypted_message.decode(), key)
        # Save decrypted file
        outname = "received_" + filename
        with open(outname, "w") as f:
            f.write(decrypted_message)
        print(f"\nReceived file: {filename} (saved as {outname})")
        conn.close()


if __name__ == "__main__":
    username = input("Enter your username: ")
    register_key()
    register_with_server(username, public_key)
    t = threading.Thread(target=receive_message, daemon=True)
    t.start()
    input("Press Enter to exit...\n")
