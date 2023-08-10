def str_reverse(w):
    v=[]
    for i in range(len(w)-1,-1,-1):
        v+=[w[i]]

print(v)

def str_reverse_inplace(w):
    rev = ""
    for c in w:
        rev = (c + rev)
    return rev


w=str(input())  
# rev_list = str_reverse(w)
# rev_str = ''.join(rev_list)
# print(rev_str)

rev = str_reverse_inplace(w)
print(rev)