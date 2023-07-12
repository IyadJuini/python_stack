class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
    

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"YOUR INT RATE :{self.int_rate} & YOUR BALANCE IS : {self.balance}")
        # your code here

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_account(self):
        self.account.display_account_info()
        return None


GON = User ("Gon","yad.juini@gmail.com")
Account1 = BankAccount(0.01, 4000)


print (GON.account.balance)