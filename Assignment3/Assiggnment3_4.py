# Assignment3_4.py

def freq(lst, target):
    return lst.count(target)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
    search = int(input("Element to search: "))
    print(f"Frequency of {search}:", freq(lst, search))
