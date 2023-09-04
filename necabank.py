class Atm:
    def __init__(self, initial_deposit):
        self.current_balance = initial_deposit

    def __sufficient_balance(self, amount):
        if amount <= self.current_balance:
            return True
        return False
        
    def deposit(self, amount):
        self.current_balance += amount
        return True

    def withdraw(self, amount):
        if self.__sufficient_balance(amount):
            self.current_balance -= amount
            return True
        return False

    def balance(self):
        return self.current_balance
    


def success_message(action, amount):
    return f'''
    =================================================
              Transaction successful!😊🎉🎉  
          You successfully {action} ${amount}.
    =================================================
    '''

def main():
    answer = 'y'
    greeting ='''
    =================================================
                       Welcome!                     
            This is the NECA Trust Bank🐘            
        We are here to bring your funds close to you
    =================================================
    '''

    request ='''
=================================================
Please enter your initial deposit: 
>>>>>>> '''
    
    try_again_message ='''
=================================================
                Invalid input😢                    
                Please try again           
=================================================
    '''

    main_menu='''
=================================================
                    Awesome!!!!
            What would you like to do?
            1. Check Balance
            2. Withdraw money
            3. Deposit money                     
=================================================
>>>>>>> '''

    withdrawal_message='''
=================================================
How much are you withdrawing?
>>>>>>> '''


    unsuccess_message ='''
    =================================================
                Transaction unsuccessful😢                     
    =================================================
    '''

    insufficient_funds_message ='''
    =================================================
                Transaction unsuccessful😢
        You don't have enough balance in your account
    =================================================
    '''



    thank_you_message ='''
    =================================================
            Thank you for banking with us!😊                     
    =================================================
    '''


    print(greeting)
    try:
        initial_deposit = float(input(request))
        newAccount = Atm(initial_deposit)
        while answer == 'y':
            response = int(input(main_menu))
            assert 0 < response < 4
            match response:
                case 1:
                    print(f"Your Account balance is: {newAccount.balance()}")
                case 2:
                    withdrawal_amount = int(input(withdrawal_message))
                    if newAccount.withdraw(withdrawal_amount):
                        print(success_message('withdrew', withdrawal_amount))
                    else:
                        print(insufficient_funds_message)
                case 3:
                    deposit_amount=float(input("Enter the amount to be deposited:"))
                    result = newAccount.deposit(deposit_amount)
                    if result:
                        print(success_message('deposited', deposit_amount))
                    else:
                        print(unsuccess_message)
            answer = input('Want to do something else? (y/n)')
        print(thank_you_message)
    except AssertionError:
        print("Response should be between 1 to 3")
    except:
        print(try_again_message)
        


main()