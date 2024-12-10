class Rectangle:
    def __init__(parameter,length,width):
        parameter.length = length
        parameter.width = width

    def area(parameter):
        print (parameter.length * parameter.width)    

    def perimeter(parameter):
        print ( 2 * (parameter.length + parameter.width))    

my_rectangle = Rectangle(int(input('length: ')), int(input('width: ')))
print (my_rectangle.area())
print (my_rectangle.perimeter())