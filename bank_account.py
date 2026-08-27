class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance!")

    def __str__(self):
        return f"{self.owner}: {self.balance}$"

acc = BankAccount("Sara", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)
