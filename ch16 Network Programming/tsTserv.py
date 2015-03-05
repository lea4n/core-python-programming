"""
This server returns timestamps
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        sendData = '[%s] %s'%(ctime(), data)
        tcpCliSock.send(sendData.encode())

    tcpCliSock.close()
tcpSerSock.close()