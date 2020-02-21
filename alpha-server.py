#!/usr/bin/python3
import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 8080)
sock.bind(server_address)
sock.listen(1)
while True:
    connection, client_address = sock.accept()
