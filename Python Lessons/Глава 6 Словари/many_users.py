users = {
	'aeinstein': { 
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {	
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}
for username, user_info in users.items():
	print(f"Username: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"Full name: {full_name.title()}")
	print(f"Location: {location.title()}\n")
	for key,value in user_info.items():
		print(f"{key} {value}")