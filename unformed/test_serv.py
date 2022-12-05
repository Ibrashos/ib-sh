import socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 8888))
	while True:
		data = s.recb(4096)
		if not data:
			continue
		st = data.decode("ascii")
		s.send(str(result)+'\n'.encode('utf-8'))
finally:
	s.close()