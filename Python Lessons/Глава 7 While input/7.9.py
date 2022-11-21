sandwich_orders = ['monako','alexandria','pastrami','hotsan','pastrami','lukan','pastrami']
finished_sandwich = []
print("All pastrami sold")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwich = sandwich_orders
print(finished_sandwich)

