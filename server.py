# Python3 program imitating a clock server

from functools import reduce
from dateutil import parser
import threading
import datetime
import socket
import time

# datastructure used to store client address and clock data
client_data = {}
vecclocserver=[1,2,3,4,5,6,7,8,9,10]
''' nested thread function used to receive
	clock time from a connected client '''
def startSendingTime(slaveclient):
    while True:
        # provide server with clock time at the clientt
        for data in range(len(vecclocserver) + 1):
            slaveclient.send(str(data).encode())
            print("Recent time " +data +"sent successfully",
                  end="\n\n")
            time.sleep(6)
        # slaveclient.send(str(
        #     datetime.datetime.now()).encode())
        # dat=str(datetime.datetime.now())

        time.sleep(6)
def beginacceptingtime(Server):
    # recieve a vector clock from client
    while True:

        # receive data from the server
        Synchronized_time =Server.recv(1024).decode()

        print("Synchronized time at the client is: " + \
              str(Synchronized_time),
              end="\n\n")


def startReceivingClockTime(connector, address):
    while True:
        # receive clock time
        data= connector.recv(1024).decode()
        # clock_time = data
        # clock_time_diff = datetime.datetime.now() - \
        #                   clock_time

        client_data[address] = {
            "data"	: data,
            "connector"	: connector
        }
        print(client_data)
        print("At "+str(datetime.datetime.now())+" clock value is",data," was recieved from client")

        print("Client Data updated by Server with :  "+ str(address),
              end = "\n\n")
        time.sleep(6)


''' Below function used to open portal for
	accepting clients over a given port of choice '''
def startingconnection(Server):

    # fetch clock time at slaves / clients
    while True:
        # accepting a client / slave clock client
        master_slave_connector, addr = Server.accept()
        slave_address = str(addr[0]) + ":" + str(addr[1])

        print(slave_address + " got connected successfully")

        current_thread = threading.Thread(
            target = startReceivingClockTime,
            args = (master_slave_connector,
                    slave_address, ))
        current_thread.start()


# subroutine function used to fetch average clock difference
def getAverageClockDiff():

    current_client_data = client_data.copy()

    for client_addr,client  in client_data.items():
        sum_of_the_clock_difference = sum(int(client['address']['data']))

        avg_items = sum_of_the_clock_difference \
                    / len(client_data)

        return avg_items

    # sum_items=0
    # for client_addr,client  in client_data.items():
    #     for client['data'] in client:
    #         sum_items =
    #         avg_items = sum_items / len(client_data)
        # sum_items =
        # avg_items=sum_items/len(client_data)



''' below function used to generate
	cycles of clock synchronization in the network '''
def synchronizeAllClocks():

    while True:

        print("\n\n New synchronization cycle started.")
        print("Number of clients to be synchronized are : " + \
              str(len(client_data)))

        if len(client_data) > 0:

            average_clock_difference = getAverageClockDiff()

            for client_addr, client in client_data.items():
                try:
                    for clk in range(len(vecclocserver)+1):
                        synchronized_time = clk + average_clock_difference

                        client['connector'].send(str(
                            synchronized_time).encode())


                except Exception as e:
                    print("Something went wrong while " + \
                          "sending synchronized time " + \
                          "through " + str(client_addr))

        else :
            print("No client data recieved. " + \
                  " Synchronization not applicable at the moment waiting for a client.")

        print("\n\n")

        time.sleep(6)


# function used to initiate the Clock Server / Master Node
def initiateClockServer(port = 4999):
    cnt=0

    Server = socket.socket()
    Server.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR, 1)

    print("Socket at master node/Server created successfully\n")

    Server.bind(('', port))

    # Start listening to requests at most 3
    Server.listen(3)
    print("Clock server at "+str(datetime.datetime.now())+" started...\n")

    # start making connections
    print("Starting to make connections...\n")
    master_thread = threading.Thread(
        target = startingconnection,
        args = (Server, ))
    master_thread.start()

    # start synchronization
    print("Starting synchronization ...\n")
    sync_thread = threading.Thread(
        target = synchronizeAllClocks,
        args = ())
    sync_thread.start()



# Start function
if __name__ == '__main__':

    # Trigger the Clock Server
    initiateClockServer(port = 4999)
