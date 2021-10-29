import datetime

user = input('What is your name \n').capitalize()
allowed_user = ['Tashy', 'TOla', 'Temi']
allowed_pass = ['passtashy', 'passtola', 'passtemi']
x = datetime.datetime.now()
deposit = 100000
running = True

while running:
    if (user in allowed_user):
        password = input('Enter your password? \n')
        userId = allowed_user.index(user)
        if (password == allowed_pass[userId]):
            print('Welcome back %s' % user)
            print(x)

            print('These are the available option: ')
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Complaint')

            option = int(input('Select an option: \n'))
      

            if (option == 1):
                print('you selected %s' % option )
                withdraw_amt = int(input('How much would you like to withdraw \n'))
                if (withdraw_amt > deposit):
                    print("Amount is too large " )
                else:
                    print('Take your cash')
                    deposit -= withdraw_amt
                    print('Your new balance is %s'% deposit)
                                
            
            elif (option == 2):
                print('you selected %s' % option )
                deposit_amt = int(input("How much would you like to deposit \n"))
                deposit += deposit_amt
                print( 'Your new balance is %s'% deposit)

            elif (option == 3):
                print('you selected %s' % option )
                complaint = input('What issue will you like to report? \n')
                print('Thank you for contacting us') 
            

            else:
                print('Invalid option, try again')
        
        else:
            print('Password incorrect, try again later')
    else:
        print('Name not found, try again later')
    print('Do you want to perform another transaction y/n')
    trans = input()
    if trans == 'y':
        pass
    elif trans == 'n':
        print('Thanks for using our service')
        running = False

    
