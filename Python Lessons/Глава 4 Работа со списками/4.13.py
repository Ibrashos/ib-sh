dishes = ('cutlet','chicken','beef stroganoff','sushi','kanapi cream')
print("Original dishes")
for dish in dishes:
	print(dish)

#Изменение кортежа происходит с ошибкой
#dishes[0] = 'beef'

print("\nNew dishes")
dishes = ('bananas','potato','beef stroganoff','sushi','kanapi cream')
for dish in dishes:
	print(dish)