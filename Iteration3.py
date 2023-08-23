import socket
import ssl
import http.client

# define the server and port to connect to
server = "www.w3.org"
port = 443

# create a TCP socket and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))

# create an SSL context and configure it with default encryption settings
ssl_ctx = ssl.create_default_context()

# wrap the socket with SSL/TLS encryption using the SSL context
ssl_sock = ssl_ctx.wrap_socket(sock, server_hostname=server)

# send an HTTPS GET request to the server
conn = http.client.HTTPSConnection(server)
conn.request("GET", "/")
response = conn.getresponse()

# read the response from the server and print it
data = response.read()
print(data)

# close the connection
conn.close()
