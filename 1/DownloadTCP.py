import socket

# Set the host and port for the web page you want to download
host = 'www.stackoverflow.com'
port = 80

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send an HTTP GET request for the web page
request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
client_socket.send(request.encode())

# Receive the response from the server
response = b''
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

# Close the socket
client_socket.close()

# Print the response
print(response.decode())
