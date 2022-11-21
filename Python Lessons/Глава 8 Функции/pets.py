def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry') # Именованные аргументы

def describe_pet2(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet2(pet_name='harry')
describe_pet2(pet_name='harry', animal_type='cat')
describe_pet2('harry')