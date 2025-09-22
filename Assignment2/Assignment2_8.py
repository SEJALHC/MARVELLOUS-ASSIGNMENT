# Assignment2_8.py

def print_reverse_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print_reverse_pattern(num)
