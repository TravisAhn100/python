# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow',}
'''''
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update
capitals.pop
capitals.popitem
capitals.clear

Key : Value
what's .items()?

items = capitals.items()

for key, value in capitals.items():
    print(f"{key} : {value}")
'''''
key = capitals.keys()

for key in capitals.keys():
    if key == 'India':
        print('MYLIFEMYRULESMYSTYLEMYATTITUDE')