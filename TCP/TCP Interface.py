# -------------------------------------------------- #
# 1. Connect TCP socket 
# 2. Update tag on central PC "Pi_x_connected = 1". 
#    Central PC needs to init these tags, also reset these tags upon disconnection.
# 3. Listen to incoming TCP message, (use non-blocking socket.recv, catch errno 11).
# -------------------------------------------------- #

import socket
import time

pts_busy = 1

# Specify PTS IP address below. Use "127.0.0.1" if using localhost.
#
TCP_IP='192.168.1.92' 
TCP_PORT=6340
BUFFER_SIZE=1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

# Send command to start PTS
MESSAGE = "View DAQ"
MESSAGE_SIZE = len(MESSAGE)

s.send(chr(MESSAGE_SIZE).encode('utf-32-be'))
s.send(MESSAGE.encode())

BUFFER_SIZE = s.recv(4)
Response = s.recv(1024)

# Wait a couple seconds for PTS to start running, then starting polling PTS status tag.
time.sleep(2)

# Keep polling PTS test process status, by checking tag value "PTS_Busy".
# If tag "PTS_Busy" is cleared (set to 0), it means that PTS measurement is complete.
while pts_busy != 0:
    MESSAGE = "Read DBL >> PTS_Busy"
    MESSAGE_SIZE = len(MESSAGE)

    s.send(chr(MESSAGE_SIZE).encode('utf-32-be'))
    s.send(MESSAGE.encode())

    BUFFER_SIZE = s.recv(4)
    Response = s.recv(1024)
    print(Response.decode('UTF-8'))
    pts_busy = float(Response.decode('UTF-8').split('=')[1].strip())
    time.sleep(1)

# PTS measurements are done by now.
# Read PTS measurements statistic tags (Avg, Min, Max). Tag's name example: "PowerRail_P_Avg"
MESSAGE = "Read DBL >> VLDO4M_SOC_P_Avg"
MESSAGE_SIZE = len(MESSAGE)

s.send(chr(MESSAGE_SIZE).encode('utf-32-be'))
s.send(MESSAGE.encode())

BUFFER_SIZE = s.recv(4)
Response = s.recv(1024)

test_tag = float(Response.decode('UTF-8').split('=')[1].strip())
print(test_tag)
print(Response.decode('UTF-8'))

input("Press Enter to continue ...")
s.close()