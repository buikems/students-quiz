class My_car:
    def __init__(self,seat,speed,age):
        self.seat = seat
        self.speed = speed
        self.age = age

    def go(self):
        return 'Vrooooooooooooom!'
    
    def guarantee(self):
        if self.age < 15:
            print('You have a guarantee')
     



mercedes = My_car(4,'Fast',10)    
print (f'Mercedes has {mercedes.seat} seats')
print (mercedes.speed)

Volvo = My_car(2,'slow',4)    
print (f'Volvo has {Volvo.seat} seats')
print (f"Volvo is {Volvo.speed}")


Tesla= My_car(6,'Very Fast',12)    
print (mercedes.seat)
print (mercedes.speed)
