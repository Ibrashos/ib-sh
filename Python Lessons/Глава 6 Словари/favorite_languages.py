favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jony': '',
    'max': '',
    }
for key, value in favorite_languages.items():
    print(f"\n{key.title()}'s favorite languages are:")
    for language in value:
        print(f"\t{language.title()}")

