import socket
import pickle

# section 5 starts at 1:03


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5555
        self.ADDR = (self.SERVER, self.PORT)
        self.p = self.connect()

    def getPos(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
