current_users = ['kyle','mike','bRIck','dina','edward']

current_users_new = []
for current_user in current_users:
	current_users_new.append(current_user.lower())
current_users = current_users_new[:]

new_users = ['olaf','linda','kyle','nick','dina']
for new_user in new_users:
	if new_user in current_users:
		print(f"{new_user.title()} Please choose another name")
	else:
		print(f"{new_user.title()} You can take this name")
