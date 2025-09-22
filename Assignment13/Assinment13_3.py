class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum_factors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_factors += i
        return sum_factors == self.Value

    def Factors(self):
        print(f"Factors of {self.Value} are:", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum_factors = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum_factors += i
        print(f"Sum of factors of {self.Value} is: {sum_factors}")
        return sum_factors


num = Numbers(28)
print("Is Prime:", num.ChkPrime())
print("Is Perfect:", num.ChkPerfect())
num.Factors()
num.SumFactors()
