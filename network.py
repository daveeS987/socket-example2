import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5555
        self.ADDR = (self.SERVER, self.PORT)
        # this will be player 0 or 1
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            # when network gets initialized
            self.client.connect(self.ADDR)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)
