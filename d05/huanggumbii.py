import turtle 
def num(x,y,evennum_list):
    x=x+y
    y=x+y
    
    if_over = (not x_in_range or not y_in_range)
    if if_over:
        return evennum_list
    else:
        return num(x,y,evennum_list)
list=[]
print(num(1,2,list),sum(list))
turtle.shape('turtle')
while True:
    turtle.forward(100)
