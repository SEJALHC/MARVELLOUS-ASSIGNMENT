# Assignment2_2.py

def star_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    num = int(input("Enter number: "))
    star_pattern(num)
