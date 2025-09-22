# Assignment2_5.py

def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Sum:", sum_of_numbers(num))
