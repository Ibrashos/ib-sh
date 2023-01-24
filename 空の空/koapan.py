import socket
import smtplib
from getpass import getpass
from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org/').text

email = 'ibrashos@yandex.ru'
password = 'ceujuxgivahidsat'
dest_email = 'ibrashos@gmail.com'
subject = 'IP'
email_text = f'HOST: {hostname}\nLocal IP: {local_ip}\nGlobal IP: {public_ip}'

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,dest_email,subject,email_text)

server = smtplib.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()

# print(f'Хост: {hostname}')
# print(f'Local IP: {local_ip}')
# print(f'Global IP: {public_ip}')