#import socket module 
from socket import *
import webserver

server = webserver.Server()
server.route("/")
server.listen()