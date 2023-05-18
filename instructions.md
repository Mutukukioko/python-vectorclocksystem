# Distributed System Vector Clock

This is a client-server application implemented in Python to demonstrate the concept of vector clocks for synchronizing clients in a distributed system.

## Overview

The application consists of a message service comprising a server process and three client processes. Each client process connects to the server over a socket, and the server is designed to handle all three clients concurrently. The clients maintain vector clocks, and the messages exchanged via the message service are limited to these vector clocks.

## Steps to Run the Application

1. Open your Python IDE and navigate to the project folder.

2. Run the server using the `server.py` script. It will start listening for data sent from the client programs via port 4999. Initially, since there is no data being received, the server console will display:

   ```
   New synchronization cycle started.
   Number of clients to be synchronized: 0
   No client data received. Synchronization not applicable at the moment. Waiting for a client.
   ```

3. Run the client using the `client.py` script. The client console will listen for any data sent by the server and also generate and send its own data to the server. The server console will display the following after a client is initiated:

   ```
   127.0.0.1:56212 got connected successfully
   At 2022-04-11 19:35:07.768868, data was received from client
   Client Data updated by Server with: 127.0.0.1:56212
   New synchronization cycle started.
   Number of clients to be synchronized: 1
   ```

4. Run the next client programs, `client2.py` and `client3.py`, individually. Each program will execute similarly to `client.py`, and the server console will show the updated number of connected clients:

   ```
   New synchronization cycle started.
   Number of clients to be synchronized: 3
   ```

5. To stop the application, terminate the `server.py` program. The client programs will also stop executing.

Note: Make sure to adjust the port numbers and IP addresses if necessary, based on your network configuration.

Feel free to explore the code and experiment with different scenarios to gain a better understanding of vector clocks in distributed systems.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Running the Server:**

To run the server, use the following command:

```
python server.py
```

**Running the Clients:**

To run the clients, use the following commands:

For `client.py`:
```
python client.py
```

For `client2.py`:
```
python client2.py
```

For `client3.py`:
```
python client3.py
```

Make sure you have Python installed on your system and the necessary dependencies are installed as mentioned in the project's requirements.

---

**Note:** This documentation assumes you have Python and the required dependencies installed.