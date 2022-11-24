import socket
from threading import Thread
s = socket.socket()
# 127.0.0.1
s.bind(('192.168.1.13', 5000))
s.listen(2)
print("Server is up now!")

conn1, add1 = s.accept() #Сохранение объекта сокета нашего клиента и его адрес
print("First client is connected to ", add1)

conn2, add2 = s.accept()
print("Second client is connected to ", add2)

def acceptor1():
	while True:
		a = conn1.recv(1024)
		conn2.send(a)
def acceptor2():
	while True:
		b = conn2.recv(1024)
		conn1.send(b)

tread1 = Thread(target=acceptor1)
tread2 = Thread(target=acceptor2)
tread1.start()
tread2.start()



