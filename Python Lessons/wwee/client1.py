import socket
from threading import Thread
# 127.0.0.1
client_socket = socket.socket() #Создаем новый сокет
client_socket.connect(("192.168.1.13", 5000)) #Подключаем его к серверному сокету

#Создаем ф-и отправки и полученя сообщений
def sender():
	while True:
		a = input() #Читаем строку с клавиатуры
		client_socket.send(a.encode("utf-8")) #Отправляем её, предварительно закодировав
def reciver():
	while True:
		message = client_socket.recv(1024) #Получаем строкуот сервера
		print(message.decode("utf-8")) #Печатаем, предварительно раскодировав

#Создаем по отдельнмоу потоку для каждой функции
tread1 = Thread(target=sender)
tread2 = Thread(target=reciver)
tread1.start()
tread2.start()