
def countdown(sec):
    print(sec)
    sec-=1
    if sec<=0:   
        return "발 싸 !"
    return countdown(sec)

print(countdown(100))