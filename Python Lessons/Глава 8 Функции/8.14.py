def make_car(prod, car_model, **options):
	options['prod'] = prod
	options['car model'] = car_model
	return options
print(make_car('subaru', 'outback', color = 'blue', tow_package = True))