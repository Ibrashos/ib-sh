import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.10.0.45', 8888))
result = s.recv(1024)
print('Message:', result.decode())
s.close()
    # quit = input("Введите 'q' для выхода: ")
    # if quit == 'q':
    #     break