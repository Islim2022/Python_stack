class BankAccount:
    def __init__(self, account, int_rate, balance):
        self.account = account
        self.int_rate = 0.01
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return self
        else:
            amount > self.balance
            self.balance = self.balance - 5
            return print('Insufficient funds: Charging a $5 fee')
    
    def display_account_info(self):
        return self.balance

    def yield_interest(self, amount):
        self.balance = amount * 0.01 + amount
        return self

Account_1 = BankAccount('Hanei\'s Account',0,0)
Account_2 = BankAccount('Zaid\'s Account',0,0)
Account_3 = BankAccount('Noor\s Account',0,0)

Account_1.deposit(100).deposit(150).deposit(200).withdraw(200).display_account_info()
Account_2.deposit(200).deposit(250).withdraw(100).withdraw(100).withdraw(50).withdraw(100).display_account_info()
Account_3.withdraw(100)
print(Account_1.balance)
print(Account_2.balance)
print(Account_3.balance)
        