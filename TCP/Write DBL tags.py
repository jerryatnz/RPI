import socket

TCP_IP='127.0.0.1'
TCP_PORT=6340
BUFFER_SIZE=1024
#MESSAGE = "Hello there!~"
#MESSAGE = "Read double >> DMM_Reading"
#MESSAGE = "Msg >> Module A >> Action X"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

for x in range(0, 10000):
    #Write tag Raw_1
    Raw_1=x*0.1
    MESSAGE = "Write DBL >> Raw_1=%d" % (Raw_1)
    MESSAGE_SIZE = len(MESSAGE)

    s.send(chr(MESSAGE_SIZE).encode('utf-32-be'))
    s.send(MESSAGE.encode())

    BUFFER_SIZE = s.recv(4)
    Response = s.recv(1024)

    print(Response.decode('UTF-8'))

    #Write tag Raw_2
    Raw_2=x*0.2
    MESSAGE = "Write DBL >> Raw_2=%d" % (Raw_2)
    MESSAGE_SIZE = len(MESSAGE)

    s.send(chr(MESSAGE_SIZE).encode('utf-32-be'))
    s.send(MESSAGE.encode())

    BUFFER_SIZE = s.recv(4)
    Response = s.recv(1024)

    print(Response.decode('UTF-8'))

input("Press Enter to continue ...")
s.close()