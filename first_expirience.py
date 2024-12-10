












class Rectangle():
    def __init__(self,length,width) :
        self.length = length
        self.width = width
        self.length= 12
    def area(self):
        return self.length * self.width 
    



my_rectangle = Rectangle(3,4)

a = my_rectangle.area()

print(a)
          