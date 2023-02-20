#Server
from socket import *
import time

# Create a server socket
server_socket = socket()

# Define the host and port to listen on
host = gethostname()
port = 6900

# Bind the socket to the host and port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(1)

print("Proxy server is running and listening for incoming connections.")

# Accept an incoming connection
client_socket, client_address = server_socket.accept()

# Read the request from the client
request = client_socket.recv(4096).decode()

# Get the IP address from the request
ip_address = request.split()[4]

print(f"Received a request from client {client_address}. IP address is {ip_address} at {time.ctime()}")

# Connect to the destination server
destination_socket = socket()
destination_port = 80

try:
    destination_socket.connect((ip_address, destination_port))
    print(f"Sending the client's request to the destination server at {time.ctime()}")
    destination_socket.send(request.encode())
except error:
    error_msg = "Error! Could not reach the destination server."
    client_socket.send(error_msg.encode())
    print(error_msg)

# Receive the response from the destination server
response = destination_socket.recv(4096).decode()

print(f"Received a response from the destination server at {time.ctime()}")

# Send the response back to the client
client_socket.send(response.encode())
print(f"Sent the response to the client at {time.ctime()}")

# Close the sockets
destination_socket.close()
client_socket.close()
server_socket.close()
