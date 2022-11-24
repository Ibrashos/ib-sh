import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a = input()
s.send(str(a), ('192.168.1.13', 8888))