pizzas = ['peperoni','markedoni','felicia']
friend_pizzas = pizzas[:]
pizzas.append('dieri')
friend_pizzas.append('western')
print("My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza.title())
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza.title())