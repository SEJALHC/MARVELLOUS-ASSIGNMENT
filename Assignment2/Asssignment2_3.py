# Assignment2_3.py

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Factorial:", factorial(num))
