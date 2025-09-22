# Assignment2_10.py

def print_factors_reverse(n):
    for i in range(n, 0, -1):
        if n % i == 0:
            print(i, end=" ")

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Factors in reverse order:")
    print_factors_reverse(num)
