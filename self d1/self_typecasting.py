#typecasting = The process of converting a vaulue of one data type to another (string, integer, float, boolean) Explicit vs implicit

#Explicit: manually converting a value of one data type
'''''
x=int(input())
for i in range(x+1):
    print(i, end = '')
'''''
x= 10
y= 8
print(round(x/y,1))