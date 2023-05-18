import socket
import datetime
import time

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 4999))

    while True:
        data = str(datetime.datetime.now())
        client_socket.send(data.encode())
        print("Sent data to server:", data)

        response = client_socket.recv(1024).decode()
        print("Received synchronized time from server:", response,"\n")

        time.sleep(2)

if __name__ == '__main__':
    client()
