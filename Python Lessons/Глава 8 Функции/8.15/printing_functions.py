def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

def print_models(unprintend_designs, completed_models):
	while unprintend_designs:
		current_design = unprintend_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)