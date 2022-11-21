responses = {}
while True:
    name = input("Enter your name: ")
    response = input("Where would you like to go ")
    responses[name] = response
    active = input("Do you want to finish?\n")
    if active == 'no':
        break
for key, value in responses.items():
    print(f"{key.title()} Would like to go {response.title()}s")