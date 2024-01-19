# while
'''''
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
'''''

# Python compound interest calculator

principle = 0
rate = 0
time = 0

'''''
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
'''''
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