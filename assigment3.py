class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def  get_info(self):
      return f'This car is a {self.brand} {self.year}'
    

my_car = Car('toyota',2020)

print(my_car.get_info()) 
