

try:
   wallet = int(input('balance: '))
except:
   print('Enter a valid input')


rice = 1200
beans = 1000
pizza = 6000
noddles = 1500





while wallet > 0:
    purchase = input('what would you like to eat? ').lower()
    if purchase == 'rice':
        if wallet > rice:
           wallet -= rice
        else:
          zero_wallet = input(f'Your wallet will run into zero,do you want to top up?: yes or no ').lower()
          if zero_wallet =='yes':
              newwallet = int(input('Topup?: '))
              wallet  += newwallet
              print(f'your balance is {wallet}')
              wallet -= rice
        print(f'your {purchase} have been delivered, you have {wallet} left')

    elif purchase == 'beans':
        if wallet > beans:
           wallet -= beans          
        else:
          zero_wallet = input(f'Your wallet will run into zero,do you want to top up?: yes or no ').lower()
          if zero_wallet =='yes':
              newwallet = int(input('Topup?: '))
              wallet  += newwallet
              print(f'your balance is {wallet}')
              wallet -= beans
        print(f'your {purchase} have been delivered, you have {wallet} left')

    elif purchase == 'noddles':
        if wallet > noddles:
           wallet -= noddles         
        else:
          zero_wallet = input(f'Your wallet will run into zero,do you want to top up?: yes or no ').lower()
          if zero_wallet =='yes':
              newwallet = int(input('Topup?: '))
              wallet  += newwallet
              print(f'your balance is {wallet}')
              wallet -= noddles
        print(f'your {purchase} have been delivered, you have {wallet} left')

    elif purchase == 'pizza':       
        if wallet > pizza:
           wallet -= pizza
        else:
          zero_wallet = input(f'Your wallet will run into zero,do you want to top up?: yes or no ').lower()
          if zero_wallet =='yes':
              newwallet = int(input('Topup?: '))
              wallet  += newwallet
              print(f'your balance is {wallet}')
              wallet -= pizza
        print(f'your {purchase} have been delivered, you have {wallet} left')        
        
else:
   newwallet = int(input('Topup?: '))
wallet += newwallet
print(f' your balance is {wallet}')
      
  

   


  
   
   

       

   

   
     
     

