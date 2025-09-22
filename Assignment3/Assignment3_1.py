# Assignment3_1.py

def add_elements(lst):
    return sum(lst)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
    print("Sum of elements:", add_elements(lst))
