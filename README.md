# Docker Assignment1
Docker Assignment1
## Overview
This project consists of two Docker containers: a server and a client. The server generates a random file, calculates its checksum, and sends it to the client. The client receives the file and verifies its checksum.

Setup and Execution
1. Run the Server:
The server will create the user-defined network, the servervol volume, and start the server to listen for client connections.

bash
Copy
Edit
./fileserver.sh
This will:

Create a user-defined Docker network (mynetwork).
Create the servervol volume.
Start the server container which listens on a port (to be specified when running the container).
2. Run the Client:
The client will connect to the server, receive the file, and verify the checksum.

bash
Copy
Edit
./fileclient.sh
This will:

Create the clientvol volume.
Start the client container, which connects to the server via the user-defined network (mynetwork).
3. Accessing Container Shells:
To manually check if the file has been received:

Access the shell of the server container:
bash
Copy
Edit
docker exec -it <server_container_id> /bin/bash
Access the shell of the client container:
bash
Copy
Edit
docker exec -it <client_container_id> /bin/bash
4. Viewing Logs:
You can view the logs of the running containers to troubleshoot or monitor their status:

For the server container:
bash
Copy
Edit
docker logs <server_container_id>
For the client container:
bash
Copy
Edit
docker logs <client_container_id>
5. File Transfer and Verification:
The server creates a random file and sends it to the client along with its checksum.
The client receives the file, saves it, and verifies the checksum.
If the checksum matches, the client prints ✅ File received successfully. Checksum verified!.
Notes:
The server listens on a port passed as a command-line argument when running the container.
The containers communicate over the user-defined network (mynetwork).
Volumes servervol and clientvol are created for persisting data between the containers.
