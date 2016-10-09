# Written by Vamei
# Client side
import socket

# Address
HOST = '10.237.100.153'
PORT = 8000

request = '''GET /test.jpg HTTP/1.x
Accept: text/*


'''
# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send message
s.sendall(request.encode())
# receive message
reply   = s.recv(1024)
print('reply is: ',reply.decode())
# close connection
s.close()
