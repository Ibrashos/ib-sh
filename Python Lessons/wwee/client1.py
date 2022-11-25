import socket
from threading import Thread
# 127.0.0.1
client_socket = socket.socket() #Создаем новый сокет
client_socket.connect(("10.10.0.45", 5000)) #Подключаем его к серверному сокету

#Создаем ф-и отправки и полученя сообщений
name = input('Введите свое имя: ')
def sender():
	while True:
		a = input() #Читаем строку с клавиатуры
		mes = f"{name}: {a}"
		client_socket.send(mes.encode("utf-8")) #Отправляем её, предварительно закодировав
def reciver():
	while True:
		message = client_socket.recv(1024) #Получаем строкуот сервера
		print(message.decode("utf-8")) #Печатаем, предварительно раскодировав

#Создаем по отдельнмоу потоку для каждой функции
tread1 = Thread(target=sender)
tread2 = Thread(target=reciver)
tread1.start()
tread2.start()