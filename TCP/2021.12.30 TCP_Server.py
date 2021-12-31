from socket import *

host = "127.0.0.1"
port = 7777
received_message = ''

print('Host IP: ' + host + f'; Port #: {port}')

s = socket(AF_INET, SOCK_STREAM)
print("Socket Made")

s.bind((host, port))
print("Socket Bound")

s.listen(5)

print("Listening for connections...")

q, addr = s.accept()

'''
data = input("Enter data to be sent: ")
q.send(data.encode('utf-8'))
'''
while received_message.lower() != "exit":
    message_in_bytes = q.recv(4)
    message_size = int.from_bytes(message_in_bytes, "big")

    print(f'Incoming message size: {message_size} bytes')
    received_message = q.recv(message_size).decode('UTF-8')
    print('Received message: ' + received_message)

    reply_message = 'ACK \"' + received_message + '\"'
    message_out_size = len(reply_message)

    q.send(chr(message_out_size).encode('utf-32-be'))
    q.send(reply_message.encode())
