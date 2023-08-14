def mt_list_create():
    list_item = 0
    list = ['' for i in range(8)]
    list_len = len(list)
    array = [list, list_len , list_item ]
    return array

def list_print(array_struct):
    list_items = array_struct[2]
    print(array_struct[0:list_items],\
          '%d is the length of the list' % array_struct[1], \
          '%d is the number of items' %  array_struct[2])

def list_value_at(array_struct,jangso):
    if not jangso >= array_struct[2] and not jangso < 0:
        return array_struct[0][jangso]
    else:
        raise Exception(f"Royal with Cheese: {jangso} is out of list range [0 .. {array_struct[2]}]")
def list_add(array_struct,adding_num):
    coord = array_struct[2]
    array_struct[0][coord]= adding_num
    array_struct[2]+=1

array = mt_list_create()
list_add(array,0)
list_print(array)

# print(list_value_at(array,2))