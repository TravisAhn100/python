class Array_list():
    
    ### Constructor
    ### 생성자: 시작할 떄(class틀을 가지고, 
    ### 객체(Object)를 하나 새로 찍어냈을 때, 그것을 기본적으로 세팅해주는 역할)
    def __init__(self):
        self.create_empty_list()
    
    def create_empty_list(self):
        self.list      = []
        self.capacity  = 8
        self.num_items = 0

    def print(self):
        print(self)

    def value_at(self, jangso):
        if 0 <= jangso and jangso < self.num_items:
            return self.list[jangso]
        else:
            raise Exception(f"Royal with Cheese: {jangso} is out of list range: 0 <= i < {self.num_items}")
        
    def add(self, adding_num):
        print()
        # coord = array_struct[2]
        # array_struct[0][coord]= adding_num
        # array_struct[2] += 1

    def __str__(self):
        return f"""list:\t\t{self.list}\n #items:\t{self.num_items}\ncap:\t\t{self.capacity}"""

# array = mt_list_create()
# list_add(array,0)
# list_print(array)

# print(list_value_at(array,2))
# 
x = Array_list()
x.print()
x.value_at(1)