from socket import *

host = "127.0.0.1"

print(host)

port = 7777

s = socket(AF_INET, SOCK_STREAM)

print("socket made")

s.connect((host, port))

print("socket connected!!!")

msg = s.recv(1024)

if msg.decode('ascii') == "jerry":
    print("I got jerry")
else:
    print("I did not get jerry")

print("Message from server : " + msg.decode('ascii'))
