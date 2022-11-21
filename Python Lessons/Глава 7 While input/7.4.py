topping = ""
while True:
	topping = input("Please enter your order: ").lower()
	if topping == 'quit':
		break
	else: 
		print(f"Your order {topping.title()}")
