favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jony': None,
    'max': None,
    }
for key, value in favorite_languages.items():
    if value:
        print(f"{key.title()}, у вас все отлично.")
    else:
        print(f"{key.title()}, пройдите проверку заново.")
