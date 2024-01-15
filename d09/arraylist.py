FONT_RED = "\033[31m"

class Array_list():
    
    ### Constructor
    ### 생성자: 시작할 떄(class틀을 가지고, 
    ### 객체(Object)를 하나 새로 찍어냈을 때, 그것을 기본적으로 세팅해주는 역할)
    def __init__(self):
        self.create_empty_list()
    
    def create_empty_list(self):
        self.capacity  = 4
        self.list      = [None] * self.capacity
        self.num_items = 0

    def print(self):
        print(self)

    def value_at(self, jangso):
        if self.assert_index_in_range(jangso):
            return self.list[jangso]
        
    def assert_index_in_range(self,jangso):
        global FONT_RED
        if 0 <= jangso and jangso < self.num_items:
            return True
        else:
            raise Exception(f"\a{FONT_RED}Royal with Cheese: {jangso} is out of list range: 0 <= i < {self.num_items}")
        
    def add(self, adding_num):
        coord = self.num_items
        self.list[coord]= adding_num
        self.num_items += 1

        if len(self.list) <= self.num_items:
            self.outofrange_list()

    def __str__(self):
        visible_range = self.list[:self.num_items]
        return f"""list:\t\t{visible_range}\n #items:\t{self.num_items}\ncap:\t\t{self.capacity}"""
    
    def outofrange_list(self):
        self.capacity *= 2
        mt_list = [None] * (self.capacity)
        for i in range(len(self.list)):
            n = self.list[i]
            mt_list[i] = n
        self.list = mt_list

    def insert(self,inserting_item,whichi):
        self.num_items += 1
        self.assert_index_in_range(whichi)
        if len(self.list) <= self.num_items:
            self.outofrange_list()
        for i in range (self.num_items-1 , whichi-1 , -1 ):
            self.list[i+1] = self.list[i]
        self.list[whichi] = inserting_item
        
    def remove(self,whichi):
        self.assert_index_in_range(whichi)
        self.num_items -= 1
        for i in range (whichi, self.num_items):
            self.list[i] = self.list[i+1] 
        

    """
    purpose: concatenates the content of list itself, doubling the size(# items) of the list
    example: [a, b, c].double() -> [a, b, c, a, b, c]
    """
    def double(self):
        for i in range(self.num_items):
            self.add(self.list[i])
x = Array_list()

def get_next_arg(words, i, prompt = ""):
    if (i < len(words) - 1):
        return words[i + 1]
    return input(prompt)            
    
while True:
    line  = input("[a]dd | [p]rint | [i]nsert | [r]emove | [d]ouble : ")
    words = line.split()

    i = 0
    while i < len(words):
        word = words[i]
        c    = word[0].lower() 

        if   (c == 'p'):
            x.print()
        
        elif (c == 'a'):
            to_add = get_next_arg(words, i)
            i += 1
            x.add(to_add)

        elif (c == 'i'):
            to_add = get_next_arg(words, i, "to_add: ")
            i += 1

            witch = int(get_next_arg(words, i, "index: "))
            i += 1
            x.insert(to_add, witch)
        
        elif (c == 'r'):
            witch = int(get_next_arg(words, i, "remove at: "))
            i += 1
            x.remove(witch)
        elif (c == 'd'):
            x.double()
        else:
            print(f"Unknown command: {word}")
        
        i += 1
