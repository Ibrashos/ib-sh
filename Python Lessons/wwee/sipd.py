import socket
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('10.10.0.16', 8888))
    result = s.recv(1024)
    print('Message:', result.decode())
    s.close()