class person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hello, my name is {self.name} and i am {self.age} yrars old.')    

me = person('favour', 20)
print (me.greet())




my_guy = person(40)
print (my_guy.greet())