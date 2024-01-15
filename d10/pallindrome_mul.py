def reverse_num(num):
    rev_num = 0
    while num != 0 :
        last_digit = num % 10   
        num //= 10
        rev_num *= 10 
        rev_num += last_digit
    return rev_num

def pallindrome_check(num):
    return num == reverse_num(num)
max_pal = 0
for i in range(1000):
    for j in range(i,1000):
        if pallindrome_check(i * j):
            if i * j >= max_pal:
                max_pal = i * j
            else:
                continue
print(max_pal)
