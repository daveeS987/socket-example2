import socket
from _thread import *
import pickle


PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(ADDR)
except socket.error as e:
    str(e)

server.listen(2)
print("SERVER UP: Waiting for Connections..")


def threaded_client(conn):

    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved :", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = server.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
