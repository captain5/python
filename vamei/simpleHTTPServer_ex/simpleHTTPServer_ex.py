# Written by Vamei
# Simple HTTPsERVER

import socketserver
import http.server

HOST = ''
PORT = 8000

# Create the server, SimpleHTTPRequestHander is pre-defined handler in SimpleHTTPServer package
server = socketserver.TCPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)
# Start the server
server.serve_forever()
