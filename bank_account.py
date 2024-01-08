class Account:

    def __init__ (self , account_number , account_holder, account_balance=0.0) :
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance

    def deposit(self, deposited_amount):
        if deposited_amount > 0:
            self.account_balance += deposited_amount
            print (f'{deposited_amount} deposited , new balance is {self.account_balance}')
        
        else :
            print(' deposited amount not valid ')

            

    def withdraw (self,withdrawn_amount):
        if withdrawn_amount >0:
            if self.account_balance >= withdrawn_amount : 
                self.account_balance -= withdrawn_amount
                print(f"Withdrew ${withdrawn_amount}. New balance: ${self.account_balance}")
            else :
                print("Insufficient funds. Withdrawal canceled.")
        else :
            print("Invalid withdrawan amount. Please enter a positive amount.")
    def check_balance (self,) : 
        return self.account_balance
my_account = Account(12345678 ,"wassim" ,1000000)


my_account.deposit(500.0) 

my_account.withdraw(200.0)  

current_balance = my_account.check_balance()
print(f"Current balance: ${current_balance}")

account_khalil = Account(87654321 , "khalil" , 2000000)

account_khalil.deposit(5000) 

account_khalil.withdraw(1000) 