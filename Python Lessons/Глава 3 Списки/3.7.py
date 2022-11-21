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

#3.6
print("\nI bought a new dining table!, more guests!")
guest.insert(0, 'edward')
guest.insert(2, 'eleonora')
guest.append('jony')
print(f"\nHello, {guest[0].title()} {invite_message}")
print(f"Hello, {guest[1].title()} {invite_message}")
print(f"Hello, {guest[2].title()} {invite_message}")
print(f"Hello, {guest[3].title()} {invite_message}")
print(f"Hello, {guest[4].title()} {invite_message}")
print(f"Hello, {guest[5].title()} {invite_message}")

#3.7
print("\nOh no, only two will come!")
popped_guest = guest.pop(0)
cant_guest = [popped_guest,]
popped_guest = guest.pop(2)
cant_guest.append(popped_guest)
popped_guest = guest.pop(2)
cant_guest.append(popped_guest)
popped_guest = guest.pop(2)
cant_guest.append(popped_guest)
print(f"Sorry man, but im kick you {cant_guest[0]}")
print(f"Sorry man, but im kick you {cant_guest[1]}")
print(f"Sorry man, but im kick you {cant_guest[2]}")
print(f"Sorry man, but im kick you {cant_guest[3]}")
print(f"\n{guest[0].title()} and {guest[1].title()} {invite_message}")
del guest[0]
del guest[0]
print(guest)