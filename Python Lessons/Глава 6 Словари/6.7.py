human_0 = {
    'first_name':'lux',
    'last_name':'kierra',
    'age':'22',
    'city':'montreal'
    }
human_1 = {
    'first_name':'max',
    'last_name':'gruvin',
    'age':'18',
    'city':'tanenberg'
    }
human_2 = {
    'first_name':'aboni',
    'last_name':'sienna',
    'age':'24',
    'city':'paris'
    }
people = [human_0,human_1,human_2]
for human in people:
    full_name = f"{human['first_name']} {human['last_name']}"
    print(f"Hello! My name {full_name.title()}")
    print(f"Im old {human['age']}")
    print(f"Im live in {human['city'].title()}\n")