from socket import *
from endpoint import Endpoint
import httpResponse

TCP_HOST = gethostname()
BUFF_SIZE = 1024

class Server:
    def __init__(self):
        self.routes = {}

    # Argument taking decorators should return a function
    def route(self, path, method="GET"):
        # Handle if I pass a route in as the func
        def decorator(func): # How do I call this?
            self.routes[path] = Endpoint(func)
        return decorator

    def __getitem__(self, key):
        try:
            return self.routes[key]
        except:
            return Endpoint()

    def listen(self, port=0):
        serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET: IPv4 addresses, 
        serverSocket.bind(('', port)) # 0 will choose random free port
        serverSocket.listen(1)
        print(f"Server lisetning on {serverSocket.getsockname()}")
        while True: 
            #Establish the connection 
            print('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()
            try: 
                message = connectionSocket.recv(BUFF_SIZE).decode() #Why decode?
                path = message.split()[1]
                response = self[path].response()
                print(response)
                connectionSocket.send(response.encode())
                connectionSocket.close()
            except: 
                connectionSocket.close()
        serverSocket.close()     
