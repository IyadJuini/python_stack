class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        # -------append-----
        BankAccount.all_accounts.append(self)
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
    def yield_interest(self):
        # your code here
        if self.balance > 0 :
            self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()   


GON = BankAccount (0.02, 560)
GON.deposit(100).deposit(40).deposit(10).withdraw(400).yield_interest().display_account_info()
print(GON.balance)


KILLUA = BankAccount (0.05, 7000)
KILLUA.deposit(500).deposit(8000).withdraw(1500).withdraw(400).withdraw(500).withdraw(600)
print(KILLUA.balance)

BankAccount.print_all_accounts()
