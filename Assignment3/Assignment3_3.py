# Assignment3_3.py

def min_element(lst):
    return min(lst)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
    print("Minimum element:", min_element(lst))
