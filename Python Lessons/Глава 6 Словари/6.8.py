jack = {
	'type': 'dog',
	'owner': 'kira'
}
moony = {
	'type': 'cat',
	'owner': 'luka'
}
pets = [jack,moony]
for pet in pets:
	print(f"Type: {pet['type'].title()} Owner: {pet['owner'].title()}")