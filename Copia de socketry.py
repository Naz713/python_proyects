#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 23:13:02 2018

@author: naz
"""

import socket
import re

class socketry:
    #MSGLEN = 512

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        msg = msg+'\n'
        totalsent = 0
        MSGLEN = len(msg)
        while totalsent < MSGLEN:
            print ( "ciclo: msg len = %s, totalsent = %s" % (MSGLEN, totalsent) )
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        print ("End Message. Totalsent = %s" % (totalsent))

    def receive(self):
        chunks = []
        bytes_recd = 0
        while True:
            chunk = self.sock.recv(2048)
            print (chunk)
            if chunk == b'\n':
                print("End of the message")
                return b''.join(chunks)
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)