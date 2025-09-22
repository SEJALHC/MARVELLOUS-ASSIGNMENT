class BankAccount:
    Rate = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder: {self.Name}, Balance: {self.Amount}")

    def Deposit(self, amt):
        self.Amount += amt
        print(f"Deposited {amt}. New Balance: {self.Amount}")

    def Withdraw(self, amt):
        if amt > self.Amount:
            print("Insufficient balance!")
        else:
            self.Amount -= amt
            print(f"Withdrawn {amt}. New Balance: {self.Amount}")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.Rate) / 100
        print(f"Interest: {interest}")


acc1 = BankAccount("Alice", 1000)
acc1.Display()
acc1.Deposit(500)
acc1.Withdraw(200)
acc1.CalculateInterest()
acc1.Display()
