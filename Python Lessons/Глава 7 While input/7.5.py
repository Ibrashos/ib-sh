price = ""
while True:
	price = input("Please enter your y.old: ")
	try:
		val = int(price)
		if int(price) <= 3:
			print("Price: Free")
		elif int(price) <= 12 and int(price) > 3:
			print("Price: 10$")
		else:
			print("Price: 15$")
	except ValueError:
		print("Please enter only number!")