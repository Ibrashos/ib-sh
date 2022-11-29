def build_profile(first, last, **info):
	info['first_name'] = first.title()
	info['last_name'] = last.title()
	return info
print(build_profile('alex', 'luwisberg', location = 'germany', city = 'linxshtein', field = 'programming on C++'))