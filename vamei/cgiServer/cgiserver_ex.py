# Written by Vamei
# A messy HTTP server based on TCP socket 

import http.server
# import BaseHTTPServer
# import CGIHTTPServer

HOST = ''
PORT = 8000

# Create the server, CGIHTTPRequestHandler is pre-defined handler
server = http.server.HTTPServer((HOST, PORT), http.server.CGIHTTPRequestHandler)
# Start the server
server.serve_forever()
