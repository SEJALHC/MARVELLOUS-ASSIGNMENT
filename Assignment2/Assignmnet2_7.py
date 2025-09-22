# Assignment2_7.py

def print_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print_pattern(num)
