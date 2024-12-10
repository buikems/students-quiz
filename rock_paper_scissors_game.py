
a =['rock','paper','scissors',]





def game():
     while True:
            computer_choice = random.choice(a)
            import random
            print(computer_choice)
            user_guess = input('rock, paper or scissors?: ').lower()
        
            score = 0
            while user_guess not in a:
                  print("invalid input, please input rock or paper or scissors")
                  user_guess = input('rock, paper or scissors?: ').lower()

            else:
                  if user_guess == computer_choice:
                      print('draw')
                      score += 1
                      print (f'score: {score}')
                  elif user_guess == 'rock' and computer_choice == 'scissors':
                    print('win')
                    score += 3
                    print (f'score: {score}')   
                  elif user_guess == 'scissors' and computer_choice == 'paper':
                    print('win')
                    score += 3
                    print (f'score: {score}')
                  elif user_guess == 'paper' and computer_choice == 'rock':
                    print('win')
                    score += 3
                    print (f'score: {score}')
                  else:
                      print('fail')
                  restart = input('do you want to continue the game? y/n: ')
                  if restart == 'y':
                      game()
                  else:
                      exit()
    

game()
       