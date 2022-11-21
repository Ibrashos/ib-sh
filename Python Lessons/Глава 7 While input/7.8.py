sandwich_orders = ['monako','alexandria','lukan','hotsan']
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}")
    finished_sandwich.append(sandwich)

print(f"\nAll finished sandwich {finished_sandwich}")



