from time import time

class Student():
    name = ""
    age  = 1
    id   = 0

    def __init__(self, name, age, id):
        self.name = name
        self.age  = age
        self.id   = id
    
    def study(self, sec):
        print("studying")
        time.sleep(sec)
        print("done studying")

    def defecate(self):
        print("defecating")
    
    def say_my_name(self):
        print(f"{self.name} you are god damn right")


sasha  = Student("Sasha",  12,   12323)
walter = Student("Walter", 52, 122323)

sasha.defecate()
walter.say_my_name()
print(walter.name)
        