# Assignment2_9.py

def print_even_factors(n):
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            print(i, end=" ")

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Even factors are:")
    print_even_factors(num)
