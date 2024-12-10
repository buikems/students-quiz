from datetime import datetime,time,timedelta
import time
students = ['john doe', 'christ excel','emeka martin']
point = 0

you = input('what is your name ')

while you not in students:
    print('your name is not in the list of students')
    break
else:
    print('what is the value of 3 raise to the power of 3?')
    option1 = input(' a = 9, b = 27, c = 81, d = 108: ' )
    if option1 == 'c':
        print('you are correct')
        point += 1
    elif option1 != 'c':
        print('you are wrong') 
            
    print('what is the square root of 100? ')    
    option2 = input(' a = 100, b = 1000, c = 1000, d = 10: ' )
    if option2 == 'd':
        print('you are correct')
        point += 1
    elif option2 != 'd':
        print('you are wrong')  
        
    print('what is the square of 5? ')    
    option3 = input(' a = 25, b = 50, c = 75, d = 100: ' )
    if option3 == 'a':
        print('you are correct')
        point += 1
    elif option1 != 'a':
        print('you are wrong')         
time.sleep(6)        
score = point / 3 * 100
print (f'Congrats, {you} you scored {score}%')