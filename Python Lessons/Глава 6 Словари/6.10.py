favorite_num = {
	'Alex': [1,4,2],
	'Marina': [2,7,5],
	'Mario': [7,7,3]
	}
for key, value in favorite_num.items():
	print(f"{key.title()} likes the next numbers:")
	for num in value:
		print(f"\t{num}")