import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
message = input('Введите сообщение: ').encode('utf-8')
s.send(message)
s.close