favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
#for name, language in favorite_language.items():
	#print(f"{name.title()}'s favorite language is {language.title()}")
#for name in favorite_language.keys():
# 	print(name.title())
friends = ['phil','sarah']
for name in favorite_language.keys():
	print(f"Hello {name.title()}")

	if name in friends:
		language = favorite_language[name].title()
		print(f"\t{name.title()}, I see you love {language}")
if 'erin' not in favorite_language.keys():
		print("Erin, please take our poll!")

