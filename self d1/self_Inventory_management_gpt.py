Inventory = {}
while True:
    Input = input("Add product and quantity (or 'exit to finish): ")
    if Input.lower() == 'exit':
        break
    product, quantity = Input.split()
    quantity = int(quantity)
    if product in Inventory:
        Inventory[product] += quantity
    else:
        Inventory[product] = quantity
    print(f'Inventory: {Inventory}:')