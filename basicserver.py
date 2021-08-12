import socket
from _thread import *

# import sys  # check if this needs to be deleted or kept
from basicplayer import Player
import pickle

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


players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]


def threaded_client(conn, player):

    # When a connection is made initially, send back player object
    # Before sending -> encode and serialize data
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:

            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:

                # Whatever the current player is,
                # Send the other players object
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            # Turn into serialized pickle object for sending back
            conn.sendall(pickle.dumps(reply))

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
