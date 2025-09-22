# Assignment2_6.py

def count(n):
    return len(str(abs(n)))

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Number of digits:", count(num))
