# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall
# June 22, 2021
# direct_interface.py
# Direct interface to the opal, needs to be programmable to pull out different array values and pass them in the correct
# directions.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import socket
import array
import random
import time

# We already know static IP for the opal, this does not need to be read in.
opal_ip = '128.123.131.137'
opal_rx = 25000
opal_tx = 25001

# Need incoming datagram socket
mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Need outgoing malleable socket
sendout = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Read in a csv of: destination IP, destination port and injected delay limit (in ms)
# rx port is given, assume tx port is +1
connections = open('connections.csv').readlines()
for i in range(len(connections)):
    connections[i] = connections[i].split(',')
    connections[i][1] = int(connections[i][1])
    connections[i][2] = int(connections[i][2])

# Set up for random delays
random.seed()

# Get input data (essentially forever)
while True:
    data = mySocket.recvfrom(1024)
    values = array.array('d', data[0])
    for i in range(len(connections)):
        delay = random.randint(0, int(connections[i][2]))/1000
        time.sleep(delay)
        sendout.sendto(bytes(array.array('d', [values[i]])), (connections[i][0], connections[i][1]))