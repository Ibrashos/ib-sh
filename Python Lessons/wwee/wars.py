def narcissistic(value):
	val = list(str(value))
	result = 0
	for num in str(value):
		result += int(num)**len(val)
	return result == int(value)		