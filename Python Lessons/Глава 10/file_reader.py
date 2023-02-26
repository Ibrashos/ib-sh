with open('pi_digits.txt') as file_object:
	lines = file_object.read()
for line in lines:
	print(line.rstrip())
print(lines)
# print(contents.rstrip())