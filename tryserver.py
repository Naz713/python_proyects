#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:48:30 2018

@author: naz
"""


import socket
import re


def wait_GET(buff):
    patt = r"\r\n"
    match = re.search(patt,buff)
    if not match:
        return buff, b''
    get = r"GET"
    chunks = buff.split(patt)
    for ch in chunks:
        
        if 
    
    
    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('0.0.0.0', 12000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    buff = b''
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            buff = buff + data
            print('received {!r}'.format(data))
            if data:
                print('sending data back')
                buff, mss = wait_GET(buff)
                connection.sendall(mss)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

