from functools import reduce
import threading
import datetime
import socket
import time

# data structure used to store client address and clock data
client_data = {}
vecclocserver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def startSendingTime(slaveclient):
    while True:
        for data in range(len(vecclocserver) + 1):
            slaveclient.send(str(data).encode())
            print("Recent time " + str(data) + " sent successfully", end="\n\n")
            time.sleep(6)


def beginacceptingtime(Server):
    while True:
        Synchronized_time = Server.recv(1024).decode()
        print("Synchronized time at the client is: " + str(Synchronized_time), end="\n\n")


def startReceivingClockTime(connector, address):
    while True:
        data = connector.recv(1024).decode()
        clock_time = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")

        client_data[address] = {
            "data": clock_time,
            "connector": connector
        }
        print(client_data)
        print("At " + str(datetime.datetime.now()) + " clock value is", data, " was received from client")

        print("Client Data updated by Server with: " + str(address), end="\n\n")
        time.sleep(6)


def startingconnection(Server):
    while True:
        master_slave_connector, addr = Server.accept()
        slave_address = str(addr[0]) + ":" + str(addr[1])

        print(slave_address + " got connected successfully")

        current_thread = threading.Thread(
            target=startReceivingClockTime,
            args=(master_slave_connector, slave_address,))
        current_thread.start()


def getAverageClockDiff():
    current_client_data = client_data.copy()
    min_time = min(current_client_data.values(), key=lambda x: x['data'])['data']
    sum_of_the_clock_difference = sum((client['data'] - min_time).total_seconds() for client in current_client_data.values())
    avg_items = sum_of_the_clock_difference / len(client_data)

    return avg_items


def synchronizeAllClocks():
    while True:
        print("\n\nNew synchronization cycle started.")
        print("Number of clients to be synchronized are: " + str(len(client_data)))

        if len(client_data) > 0:
            average_clock_difference = getAverageClockDiff()

            for client_addr, client in client_data.items():
                try:
                    for clk in range(len(vecclocserver) + 1):
                        synchronized_time = (client['data'] + datetime.timedelta(seconds=average_clock_difference)).strftime("%Y-%m-%d %H:%M:%S.%f")
                        client['connector'].send(str(synchronized_time).encode())

                except Exception as e:
                    print("Something went wrong while sending synchronized time through " + str(client_addr))

        else:
            print("No client data received. Synchronization not applicable at the moment. Waiting for a client.")

        print("\n\n")
        time.sleep(6)


def initiateClockServer(port=4999):
    Server = socket.socket()
    Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Socket at master node/Server created successfully\n")

    Server.bind(('', port))
    Server.listen(3)
    print("Clock server at " + str(datetime.datetime.now()) + " started...\n")

    print("Starting to make connections...\n")
    master_thread = threading.Thread(
        target=startingconnection,
        args=(Server,))
    master_thread.start()

    print("Starting synchronization...\n")
    sync_thread = threading.Thread(
        target=synchronizeAllClocks,
        args=())
    sync_thread.start()


if __name__ == '__main__':
    initiateClockServer(port=4999)
