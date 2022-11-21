names = ['barry','oleg','oglock','admin','kyle']
for name in names:
	if name == 'admin':
		print("Hello admin, would you like to see a status report?.")
	else:
		print(f"Hello {name.title()}, thank you for logging in again")