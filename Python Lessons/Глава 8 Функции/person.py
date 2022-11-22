def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musican = build_person('jimi','hendrix', age=27)
print(musican)