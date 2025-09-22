# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a server socket
    serverSocket.bind(("", port))

    #Fill in start
    serverSocket.listen(1)  # Listen for incoming connections
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Fill in start - accepting connections
        #Fill in end

        try:
            message = connectionSocket.recv(1024).decode()  # Fill in start - receiving message
            #Fill in end
            filename = message.split()[1]

            #opens the client requested file.
            f = open(filename[1:], "r")  # fill in start - open file in read mode
            #fill in end

            #This variable can store the headers you want to send for any valid or invalid request.
            #Fill in start
            header = "HTTP/1.1 200 OK\r\n"
            outputdata = header.encode()
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
            outputdata += b"Server: MySimpleServer/1.0\r\n"
            outputdata += b"Connection: close\r\n\r\n"
            #Fill in end

            for i in f:  # for line in file
                #Fill in start - append your html file contents
                outputdata += i.encode()
                #Fill in end

            #Send the content of the requested file to the client
            #Fill in start
            connectionSocket.send(outputdata)
            #Fill in end

            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            #Fill in start
            header = "HTTP/1.1 404 Not Found\r\n"
            outputdata = header.encode()
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
            outputdata += b"Server: MySimpleServer/1.0\r\n"
            outputdata += b"Connection: close\r\n\r\n"
            outputdata += b"<html><body><h1>404 Not Found</h1></body></html>"
            connectionSocket.send(outputdata)
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

if __name__ == "__main__":
    webServer(13331)
