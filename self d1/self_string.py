'''''
result = len(name) # length of the name
result = name.find("o") finds the letter in ()
result = name.rfind("o") finds the last same letter in ()
name = name.capitalize() capitalizes the first letter?
name.upper() all capital
name.lower() all lower case
result = name.isdigit()  if there is only number, true
result = name.isalpha() if there is only alphabet, true
result = phone_number.count("-") counts the number of (inside the box) 
.replace()

if need help, print(help())
'''''

username = input("Enter your username: ")


if len(username) >= 12:
    print("Your username can't have more than 12 characters. ")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers!")
else:
    print(f"Welcome {username}!")