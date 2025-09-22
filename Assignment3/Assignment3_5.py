# Assignment3_5.py

from marv import ChkPrime

def ListPrime(lst):
    return sum(num for num in lst if ChkPrime(num))

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
    print("Sum of prime numbers:", ListPrime(lst))
