# Distributed System Vector Clock
Created client server application to demonstrate vector clock concept to synchronize the clients in a Distributed System in python.

-Implemented a message service consisting of a server process and three clients. Each client process will connect to the server over a socket. The server would be able to handle all three clients concurrently.

- Clients will maintain vector clocks, and the messages exchanged via the message service will be constrained exclusively to those vector clocks.

- Each client will maintain a vector clock. Every two to ten seconds, each client will randomly choose one other client (e.g., a unicast) and send that client its vector clock
Steps:
1.open your python IDE then open the project folder
2.First click on the server.py program and run it. It should listen listen for sent data from the clint program via the port 4999. At first there will be no data being recieved thus it will be listening for data and in the process the console will be printing
    
   New synchronization cycle started.
   Number of clients to be synchronized are : 0
   No client data recieved.  Synchronization not applicable at the moment waiting for a client.

3.Run the client.py program. At the client.py console the program will listen for any sent data  inform of date as a string from the server and also generate a date from the client side and send it to the server.
  the server output after initiating a client:
   
    127.0.0.1:56212 got connected successfully(This is the client that sent data to the server)
    At 2022-04-11 19:35:07.768868 data was recieved from client (Here we see the time at which data was sent from the client side)
     
    Client Data updated by Server with :  127.0.0.1:56212 (Here the server sends data to the client again)

     New synchronization cycle started.(The Server then listens for any new data from different client)
     Number of clients to be synchronized are : 1 (Showing the number of clients connected)
4.Run the next client program client2.py and client3.py the program will execute as the first one for each of the programs individually and the server will show the new number of connected clients as 3

      New synchronization cycle started.
      Number of clients to be synchronized are : 3

Once you terminate the server program the client programs will also stop executing.