cars = ['audi','bmw']
if cars[0] == 'audi':
	print(True)
if 'audi' in cars[0]:
	print(True)
if len(cars[0]) == 4:
	print(True)
if len(cars[0]) >= 3:
	print(True)
if cars[0] != cars[1]:
	print(True)

# else???	
for car in cars:
	if 'bmw' not in cars:
		print("YES")
	else: print("NO")
if 'bmw' in cars:
	print("Yes")

