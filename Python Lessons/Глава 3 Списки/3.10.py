cars = ['toyota','honda','bmw','mclaren']
motorcycle = ['suzuki','dicati','yamaha']
country = ['russia','france','germany','iraq']

remove_country= country[3]  # Убираем из списка значение
country.remove('iraq')
print(f"i dont will come {remove_country.title()}")

country.append('japan') # Добавляем новое значение в список
print(f"but i want come {country[3].title()}")

print(f"i have many cars, but i take one{cars}") #Используем метод pop()
popped_cars = cars.pop(3)
print(f"i will go by {popped_cars.title()}")
print(f"the rest is in the garage.{cars}")

print("Also I have a collection of motorcycles")
print(motorcycle)

#сортировка по алфавиту
print(sorted(motorcycle))
print(f"I have {len(motorcycle)} of them") #Определение длины списка
motorcycle.insert(3,'picadili')
print(f"I am going to buy a new motorcycle {motorcycle[3].title()}")



