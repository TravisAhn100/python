import random
from time import time
p=0
while True:
    a = random.randrange(0,100)
    b = random.randrange(0,2)
    d = random.randrange(0,4)
    c =['+','-','x','/'][d]
    t= True
    if b!=0:
        l=time()
   
        print(a,c,b,'=',end=' ')
        x=int(input())
    

        if c=='+':
                if x== a+b:
                   x=t
        if c=='-':
                   x=t
                    
        if c=='x':
                if x== a*b:
                    x=t
                    
        if c=='/':
                if x== a//b:
                    x=t
        if x==t:
            p+=100
        if x!=t:
            x=False
            print('False')
            break
        print(x)
        y=time()
        print("{:.0f}".format(y-l),'sec')
print("congrats! You've earned %d points!"% p)



    
