'''''
if elif else statements
age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == 'N':
    print("NO FOOD FOR YOU")

name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")
'''''

# The calculator
import random
import time

operator = ['+','-','x','%']

start = input('The SaChickYeonSan : 30 problems, timer : press to start :')

correct_answer = 0

wrong_answer = 0

start_time = time.time()
for i in range(10):
        num1 = random.randrange(0,20)
        num2 = random.randrange(0,20)
        random_operator = random.choice(operator)
        print(f'{num1} {random_operator} {num2} = ', end='')
        x = float(input())
        if random_operator == '+':
            result = num1 + num2
            if x == result:
                correct_answer+=1
            else:
                wrong_answer+=1
        if random_operator == '-':
            result = num1 - num2
            if x == result:
                correct_answer+=1
            else:
                wrong_answer+=1
        if random_operator == 'x':
            result = num1 * num2
            if x == result:
                correct_answer+=1
            else:
                wrong_answer+=1
        if random_operator == '%':
            result = round(num1 / num2, 1)
            if x == result:
                correct_answer+=1
            else:
                wrong_answer+=1
end_time = time.time()

duration = round(end_time - start_time,2)

print(f'Congrats! It took {duration} seconds for you to finnish! You got {correct_answer} right and {wrong_answer} wrong!')