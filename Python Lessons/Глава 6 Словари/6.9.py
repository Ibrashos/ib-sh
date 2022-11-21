favorite_places = {
	'jack': {
		'first': 'monako',
		'second': 'volga',
		'third': 'russia',
	},
	'alex': {
		'first': 'kiev',
		'second': 'new york',
		'third': 'india',
	},
	'montana': {
		'first': 'zimbabwe',
		'second': 'china',
		'third': 'korea',
	},
}
for name, values in favorite_places.items():
	print(f"{name.title()} likes three places: ")
	favorite = f"{values['first'].title()}\n{values['second'].title()}\n{values['third'].title()}"
	print(f"{favorite}\n")