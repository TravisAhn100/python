#python weight converter
'''''
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is : {round(weight , 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is : {round(weight , 1)} {unit}")
else:
    print(f"{unit} was not valid")
'''''
#Python temperature converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp)/5 + 32 , 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp -32) * 5/9 , 1)
    print(f"The emperatue in Celsius isL {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")