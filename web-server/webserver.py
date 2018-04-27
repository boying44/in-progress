from socket import *
import endpoint

TCP_HOST = gethostname()
BUFF_SIZE = 1024

class Server:
    def __init__(self):
        self.routes = {}

    def route(self, path, method="GET"):
        self.routes[path] = endpoint.Endpoint("/")
    
    def __getitem__(self, key):
        try:
            return self.routes[key].response()
        except:
            return 'HTTP/1.1 404 Not Found\n\n404 Not Found\n'

    def listen(self, port=0):
        serverSocket = socket(AF_INET, SOCK_STREAM) #AF_INET: IPv4 addresses, 
        serverSocket.bind(('', port)) #0 will choose random free port
        serverSocket.listen(1)
        print(f"Server lisetning on {serverSocket.getsockname()[1]}")
        while True: 
            #Establish the connection 
            print('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()
            try: 
                message = connectionSocket.recv(BUFF_SIZE).decode() #Why decode?
                route = message.split()[1]
                response = self[route]
                connectionSocket.send(response.encode())
                connectionSocket.close()
            except: 
                connectionSocket.close()
        serverSocket.close()     
