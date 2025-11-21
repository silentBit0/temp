import socket
import threading
import json
import datetime

PUBLIC_KEYS = {}
LOG_FILE = "server_log.txt"


def log(activity):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {activity}\n")


def client_handler(conn, addr):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            request = json.loads(data.decode())
            action = request.get("action")

            if action == "register":
                username = request["username"]
                key = tuple(request["public_key"])
                PUBLIC_KEYS[username] = key
                conn.send(json.dumps({"status": "ok"}).encode())
                log(f"Registered public key for {username}: {key}")
            elif action == "get_key":
                target_user = request["target_user"]
                if target_user in PUBLIC_KEYS:
                    conn.send(
                        json.dumps(
                            {"status": "ok", "public_key": PUBLIC_KEYS[target_user]}
                        ).encode()
                    )
                    log(f"Sent public key of {target_user} to requestor")
                else:
                    conn.send(
                        json.dumps(
                            {"status": "error", "message": "User not found"}
                        ).encode()
                    )
            else:
                conn.send(
                    json.dumps(
                        {"status": "error", "message": "Unknown action"}
                    ).encode()
                )
        except Exception as e:
            log(f"Error: {e}")
            break
    conn.close()


def start_server(host="localhost", port=5001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Third-party Server running on {host}:{port}")
    log("Server started")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=client_handler, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    start_server()
