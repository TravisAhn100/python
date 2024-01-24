# format specifiers = {value:flags} format a value based on what flags are inserted
'''''
< > ^ + '' :.(n)f
'''''
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:10,.2f}")
print(f"Price 2 is ${price2:10,.2f}")
print(f"Price 3 is ${price3:10,.2f}")

x = int(input())
print(f"your number is {x:02}")