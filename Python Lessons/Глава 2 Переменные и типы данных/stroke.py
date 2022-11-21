# f Строки
first_name = "ada"
second_name = "lovelace"
full_name = f"{first_name} {second_name}"
message = f"Hello, {full_name.title()}!"
print(message)
print("\n\tPython") # Разрыв/Табуляция Текста

# Удаление пропусков
favorite = ' Python '
print(favorite.lstrip())
print(favorite.rstrip())
favorite = favorite.strip()
print(favorite)
