import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 6340
BUFFER_SIZE = 1024

#------------Connect to host-----------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#------------Send message to host-----------------
MESSAGE = "Write DBL >> Pi_1_connected = 1"
MESSAGE_SIZE = len(MESSAGE)

s.send(chr(MESSAGE_SIZE).encode('utf-32-be'))
s.send(MESSAGE.encode())

message_in_bytes = s.recv(4)
BUFFER_SIZE = int.from_bytes(message_in_bytes, "big")

print(BUFFER_SIZE)
Response = s.recv(BUFFER_SIZE).decode('UTF-8')
print(Response)

while Response.lower() != "exit":
    print("Waiting for command from host ...")
    '''
    Host to send below:
    TCP: Set Response >> Exit
    TCP: Respond
    '''
    message_in_bytes = s.recv(4)
    BUFFER_SIZE = int.from_bytes(message_in_bytes, "big")

    print(BUFFER_SIZE)
    Response = s.recv(BUFFER_SIZE).decode('UTF-8')
    print(Response)

s.close()