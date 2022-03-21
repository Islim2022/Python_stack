import BankAccount.py
class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount (int_rate = 0.01, balance = 0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        if amount < self.account:
            self.account -= amount 
            return self

    def display_user_balance(self):
        return self.account

user_1 = User('Hanei')
user_2 = User('Sam')
user_3 = User('Zaid')

user_1.make_deposit(50).make_deposit(100).make_deposit(150).make_withdrawal(25).transfer_money(user_3,200).display_user_balance()
user_2.make_deposit(300).make_deposit(200).make_withdrawal(200).make_withdrawal(50)
user_3.make_deposit(1000).make_withdrawal(400).make_withdrawal(100).make_withdrawal(100)

print(user_1.user_balance)
print(user_2.user_balance)
print(user_3.user_balance)