#import socket module 
from socket import *
import webserver
import endpoint

server = webserver.Server()
@server.route("/")
def hello():
    return 'hello, world!'

server.listen()