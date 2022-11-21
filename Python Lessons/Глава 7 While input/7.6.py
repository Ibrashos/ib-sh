price = ""
active = True
max = 1
while active:
	price = input("Please enter your y.old: ")
	if price == 'quit':
		break
	try:
		val = int(price)
		if int(price) <= 3:
			print("Price: Free")
		elif int(price) <= 12 and int(price) > 3:
			print("Price: 10$")
		else:
			print("Price: 15$")
		if max == 5:
			active = False
		max += 1
	except ValueError:
		print("Please enter only number!")