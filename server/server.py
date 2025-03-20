import socket
import os
import hashlib
import random
import string

SERVER_PORT = 5000  # Can be set via command line
FILE_PATH = "/serverdata/random_file.txt"

def generate_random_text(size=1024):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def calculate_checksum(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def main():
    os.makedirs("/serverdata", exist_ok=True)
    with open(FILE_PATH, "w") as f:
        f.write(generate_random_text())

    checksum = calculate_checksum(FILE_PATH)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on port {SERVER_PORT}")

    conn, addr = server_socket.accept()
    print(f"Client connected: {addr}")

    with open(FILE_PATH, "rb") as f:
        conn.sendall(f.read())
    conn.sendall(checksum.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
