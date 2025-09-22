# Assignment3_2.py

def max_element(lst):
    return max(lst)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
    print("Maximum element:", max_element(lst))
