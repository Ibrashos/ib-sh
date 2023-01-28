from random import choice
roll_list = [13,29,37,48,55,66,70,82,98,00,'A','I','Y','B','C']
win_list = []
roll = 0
while True:
	roll += 1
	win_list.append(choice(roll_list))
	if roll == 4:
		break
print(f"Win combination: {win_list}")