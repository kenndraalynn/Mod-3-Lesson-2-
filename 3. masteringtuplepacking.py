orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

def display_orders(orders):
    for order in orders:
        name, item, quantity = order
        print(f"Name: {name}, Item: {item}, Quantity: {quantity}")

while True:
    name = input("Please enter your name or 'stop' to exit: ")
    if name.lower() == 'stop':
        break
    item = input("What are you purchasing? ")

    quantity = input("How many? Please use numbers ")
    try:
        quantity = int(quantity)
    except ValueError:
        print("An error has occurred, please try again")
        continue

    orders.append((name, item, quantity))

display_orders(orders)