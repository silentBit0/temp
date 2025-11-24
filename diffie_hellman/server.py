import socket

def server():
    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))
    a = int(input("Enter Alice's private key a: "))

    A = pow(g, a, p)
    print("Alice's Public Key A:", A)

    server = socket.socket()
    server.bind(("0.0.0.0", 5000))
    server.listen(1)

    print("\n[+] Waiting for client connection...")
    conn, addr = server.accept()
    print(f"[+] Connected with {addr}")

    conn.send(f"{p},{g},{A}".encode())

    data = conn.recv(1024).decode()
    B = int(data)
    print("Bob's Public Key B:", B)

    secret_A = pow(B, a, p)
    print("Alice Computes Shared Secret:", secret_A)

    conn.close()
    server.close()

    print("\n[+] Connection closed.")
    print("[+] Shared Key Established:", secret_A)

server()
