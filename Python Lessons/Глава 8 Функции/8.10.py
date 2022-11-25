def send_messages(msgs,n_msgs):
	while msgs:
		msgs_pop = msgs.pop()
		print(f"{msgs_pop} (popped)")
		n_msgs.append(msgs_pop)
msgs = ['hello','bye','how are you?']
n_msgs = []
send_messages(msgs,n_msgs)
print(n_msgs)