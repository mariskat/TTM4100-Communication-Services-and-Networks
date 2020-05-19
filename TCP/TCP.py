
# Import socket module
from socket import *

# Creating TCP server socket (AF_INET is used for IPv4 protocols and SOCK_STREAM FOR TCP)
serverPort=8000 #Port number

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.38.130',serverPort)) #Binding socket to server address and server port
serverSocket.listen(1) #Listening to at most 1 connection

while True:
    print('Server ready to receive')
    connectionSocket, addr = serverSocket.accept()

    try:
        message=connectionSocket.recv(1024).decode()
        filepath=message.split()[1] #Second path of header, id [1]
        f=open(filepath[1:]) #Read path from second character

        responseHeader = "HTTP/1.1 200 \r\n\r\n"
        connectionSocket.send(responseHeader.encode())

        outputdata= f.read()

        response = outputdata+ "\r\n"
        connectionSocket.send(response.encode())

        connectionSocket.close()

    except (IOError, IndexError):
            responseHeader = "HTTP/1.1 404 \r\n\r\n"

            connectionSocket.send(responseHeader.encode())
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
            connectionSocket.close()

serverSocket.close()
