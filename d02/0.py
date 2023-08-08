import random
from time import time

while True:
    a = random.randrange(1,100)
    b = random.randrange(1,100)
    d = random.randrange(0,4)
    c =['+','-','x','/'][d]
    t= True
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
    if x!=t:
        x=False
    print(x)
    y=time()
    print("{:.0f}".format(y-l),'sec')


