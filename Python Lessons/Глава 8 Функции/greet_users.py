def greet_users(names):
	for name in names:
		msg = f"hello, {name.title()}!"
		print(msg)

username = ['hannah', 'ty', 'margot']
greet_users(username)