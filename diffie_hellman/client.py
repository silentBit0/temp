import socket

def client():
    b = int(input("Enter Bob's private key b: "))

    client = socket.socket()
    client.connect(("127.0.0.1", 5000))
    
    data = client.recv(1024).decode()
    p, g, A = map(int, data.split(","))
    print("Received from Alice -> p, g, A:", p, g, A)

    B = pow(g, b, p)
    print("Bob's Public Key B:", B)


    client.send(str(B).encode())

    secret_B = pow(A, b, p)
    print("Bob Computes Shared Secret:", secret_B)

    client.close()
    print("\n[+] Connection closed.")
    print("[+] Shared Key Established:", secret_B)

client()
