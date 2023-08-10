
def num(x,y,evennum_list):
    x_in_range = (x < 4000000)
    y_in_range = (y < 4000000)
    if x_in_range:
        if x%2==0:
            evennum_list+=[x]
    if y_in_range:
        if y%2==0:
            evennum_list+=[y]
    x=x+y
    y=x+y
    
    if_over = (not x_in_range or not y_in_range)
    if if_over:
        return evennum_list
    else:
        return num(x,y,evennum_list)
list=[]
print(num(1,2,list),sum(list))