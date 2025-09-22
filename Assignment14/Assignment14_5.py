class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

acc = BankAccount("123456", "Riya", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.display()
