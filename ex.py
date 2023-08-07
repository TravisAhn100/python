x=[]
for i in range(0,1000):
    if i%3==0:
        x+=[i]
    if i%5==0:
        x+=[i]
    if i%3==0 and i%5==0:
        x.pop()
print(sum(x))
