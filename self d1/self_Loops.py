# while
'''''
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")

# Python compound interest calculator

principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principke can't be less than or equal to zero")
while rate <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <=0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time cna't be less than or equal to zero")

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principke can't be less than or equal to zero")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")
    else:
        break
while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time cna't be less than or equal to zero")
    else:
        break
total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s: ${total:.2f}")

# for
# for x in reverse(range())

credit_card = "1234-5678-9012-3456"

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# nested loop = a loop in a loop (outer, inner)

rows = int(input("Enter the # of rows : "))
clomuns = int(input("Enter the # of columns : "))
symbol = input("Enter the # of symbol : ")

for x in range(rows):
    for y in range(rows):
        print(symbol, end=" ")
    print()
'''''

#timer
'''''
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0 , -1):
    seconds = x % 60 
    minutes = int(x/60) % 60
    hours = int(x / 3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

"""""
for x in reverse(range(0,my_time)):
    print(x)
    time.sleep(1)  
"""""

print("TIME'S UP!")
'''''
####-####-####-####

card_num =input("Enter a credit card: ")
sum_odd_digits = 0
sum_even_digits = 0
total = 0

#step1
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]

#step2
for x in card_num[::2]:
    sum_odd_digits += int(x)

#step3
for x in card_num[1::2]:
    x = int(x) * 2
    if x >=10:
        sum_even_digits += (1 + (x % 10 ))
    else:
        sum_even_digits += int(x)

total = sum_even_digits + sum_odd_digits
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")