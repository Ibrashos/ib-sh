#3.4
guest = ['arnold','linda','mark']
invite_message = "im want to invite you to my dinner"
print(f"Hello, {guest[0].title()} {invite_message}")
print(f"Hello, {guest[1].title()} {invite_message}")
print(f"Hello, {guest[2].title()} {invite_message}")

#3.5
popped_guest = guest.pop(1)
print(f"\nSorry my friend {popped_guest} cant come here")
guest.insert(1, 'diana')
print(f"\nHello, {guest[0].title()} {invite_message}")
print(f"Hello, {guest[1].title()} {invite_message}")
print(f"Hello, {guest[2].title()} {invite_message}")