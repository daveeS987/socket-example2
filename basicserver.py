import socket
from _thread import *
import pickle


port = 5555
# server = socket.gethostbyname(socket.gethostname())
server = "192.168.1.198"
ADDR = (server, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(ADDR)
except socket.error as e:
    str(e)

s.listen(2)
print("server UP: Waiting for Connections..")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):

    # player is the index, this is sending position of player
    conn.send(str.encode(make_pos(pos[player])))

    reply = ""
    while True:
        try:
            # this is position received from client
            data = read_pos(conn.recv(2048).decode())
            # update current players position
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                # if its a certain player, send the other players position
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Recieved data: ", data)
                print("Sending reply: ", reply)

            # turn reply into string before sending back
            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
