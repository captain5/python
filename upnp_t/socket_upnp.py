import socket
import os

ip_port = ('192.168.31.1',5351) 
sk = socket.socket()
sk.connect(ip_port)

filename='abc.bin'    
with open(filename, 'r') as infile:
	d = infile.read(8024)
        while d:
	    sk.sendall(d) 
            d = infile.read(8024)
	    server_reply = sk.recv(1024)
	    print server_reply

sk.close()
