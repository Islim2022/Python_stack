class User:
    def __init__(self, name):
        self.name = name
        self.user_balance = 0

    def make_deposit(self, amount):
        self.user_balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount < self.user_balance:
            self.user_balance -= amount 
            return self

    def display_user_balance(self):
        return self.user_balance

    def transfer_money(self, other_user, amount):
        if amount <= self.user_balance:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            return self

user_1 = User('Hanei')
user_2 = User('Sam')
user_3 = User('Zaid')

# user_1.make_deposit(50)
# user_1.make_deposit(100)
# user_1.make_deposit(150)
# user_1.make_withdrawal(25)
# user_1.display_user_balance()
user_1.make_deposit(50).make_deposit(100).make_deposit(150).make_withdrawal(25).transfer_money(user_3,200).display_user_balance()

# user_2.make_deposit(300)
# user_2.make_deposit(200)
# user_2.make_withdrawal(200)
# user_2.make_withdrawal(50)
user_2.make_deposit(300).make_deposit(200).make_withdrawal(200).make_withdrawal(50)


# user_3.make_deposit(1000)
# user_3.make_withdrawal(400)
# user_3.make_withdrawal(100)
# user_3.make_withdrawal(100)
user_3.make_deposit(1000).make_withdrawal(400).make_withdrawal(100).make_withdrawal(100)

print(user_1.user_balance)
print(user_2.user_balance)
print(user_3.user_balance)

