import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        print("self.server: ", self.SERVER)
        self.PORT = 5555
        self.ADDR = (self.SERVER, self.PORT)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


n = Network()
print(n.send("hello"))
print(n.send("working"))
