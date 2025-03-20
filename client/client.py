import socket
import os
import hashlib

SERVER_IP = "server_container"  # Corrected: Use the server container's name
SERVER_PORT = 5000
FILE_PATH = "/clientdata/received_file.txt"

def calculate_checksum(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def main():
    os.makedirs("/clientdata", exist_ok=True)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    with open(FILE_PATH, "wb") as f:
        data = client_socket.recv(1024)
        while data:
            f.write(data)
            data = client_socket.recv(1024)

    received_checksum = client_socket.recv(32).decode()
    client_socket.close()

    if calculate_checksum(FILE_PATH) == received_checksum:
        print("File received successfully. Checksum verified!")
    else:
        print("Checksum verification failed!")

if __name__ == "__main__":
    main()