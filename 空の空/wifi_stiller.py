import subprocess
import time

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('cp866').split('\n')

wi_Fis = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]
list = []
def still():
    for wi_fi in wi_Fis:
        results = subprocess.check_output(['netsh','wlan','show','profile',wi_fi,'key=clear']).decode('cp866').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]
        list.append({'Name': wi_fi, 'Password': results[0]})
    return list
print(list)