'''''
collection = single 'variable' used to store multiple values
List    = [] ordered and changeable. Duplicates OK
Set     = {} unordered and immutable, but ADD/REMOVE OK. No Duplicates . GOOD FOR COLOURS
Tuple   = () ordered and unchangeable. Duplicates OK. Faster

fruits = ("apple","orange","banana","coconut","coconut")
#print(dir(fruits))
#print(help(fruits))
#print(fruits[::-1])
#for fruit in fruits:
#    print(fruit)

print(fruits.count("apple"))
'''''

#shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Eneter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART ----")

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price

print()
print(f"Your total is ${total}")