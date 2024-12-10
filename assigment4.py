class Student:
    def __init__(self, name, grade,school_name):
        self.name = name
        self.grade = grade
        self.school_name = school_name

    def display(self):
        print(f'Student {self.name} is in grade {self.grade} at {self.school_name}.')    

mike = Student('mike',4,'top hills schools')    
jacob = Student('jacob',5,'western academy') 

print(mike.display()) 
print(jacob.display())