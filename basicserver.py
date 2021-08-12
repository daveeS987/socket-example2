import socket
from _thread import *
import sys


port = 5555
server = socket.gethostbyname(socket.gethostname())
ADDR = (server, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(ADDR)
except socket.error as e:
    str(e)

s.listen(2)
print("server UP: Waiting for Connections..")

# takes string -> turn into tuple
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


# takes tuple -> turn into string
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


# initialize players x,y position
# index 0 is first player, index 1 is second player
pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):

    # player is the index: 0 or 1
    # Once connect is called from network.py,
    # It will send back the position of player to connect method in network.py
    conn.send(str.encode(make_pos(pos[player])))

    reply = ""
    while True:
        try:
            # only send methods will trigger this code block

            # this is position sent from client - the current player
            data = read_pos(conn.recv(2048).decode())
            # update current players position
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                # Now send the other players position back to client
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Recieved data: ", data)
                print("Sending reply: ", reply)

            # reply is currently a tuple
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
