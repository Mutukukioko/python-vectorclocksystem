# Python3 program imitating a client process

from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket
import time
vectorclock=[1,2,3,4,5,6,7,8,9,10]

# client thread function used to send time at Server side
def startSendingTime(Server):
    # initialise vector time here
    while True:
        for data in range(1,len(vectorclock)+1):
            Server.send(str(data).encode())
            print('sending logical clock value ',data,' from client ')
            time.sleep(6)

        # provide server with clock time from the client
        # Server.send(i.encode())
        # dat = str(datetime.datetime.now())
        #
        # print("Recent time "+dat+"  sent successfully",
        #       end="\n\n")
        time.sleep(6)




# client thread function used to receive synchronized time
def beginacceptingtime(slaveclient):
    while True:
        # receive data from the server
        Synchronized_time =slaveclient.recv(1024).decode()

        print("Synchronized time at the client is: " + \
              str(Synchronized_time),
              end="\n\n")
        time.sleep(6)


# function used to Synchronize client process time
def initiatingClient(port=9000):
    slaveclient = socket.socket()

    # connect to the clock server on local computer
    slaveclient.connect(('127.0.0.1', 4999))

    # start sending time to server
    print("Starting to receive time from server\n")
    send_time_thread = threading.Thread(
        target=startSendingTime,
        args=(slaveclient,))
    send_time_thread.start()

    # start receiving synchronized from server
    print("Starting to receive " + \
          "synchronized time from server\n")
    recdtime = threading.Thread(
        target=beginacceptingtime,
        args=(slaveclient,))
    recdtime.start()


# The Start program function
if __name__ == '__main__':
    # initialize the Slave / Client
    initiatingClient(port=9000)
