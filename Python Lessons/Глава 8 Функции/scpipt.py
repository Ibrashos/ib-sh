import subprocess
command = input("Введите команду для pip ")
subprocess.run(f"pip {command}", shell=True, text=True)
