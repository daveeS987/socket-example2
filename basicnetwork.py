import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5555
        self.ADDR = (self.SERVER, self.PORT)
        # this will be the current players position
        self.pos = self.connect()

    def getPos(self):
        # this will send the position
        return self.pos

    def connect(self):
        try:
            # this will make the initial connection
            self.client.connect(self.ADDR)
            # will return the position, which will then be self.pos
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
