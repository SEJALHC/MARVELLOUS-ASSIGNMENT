from functools import reduce

input_str = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_str.split()))

product = reduce(lambda x, y: x * y, numbers)

print("Numbers:", numbers)
print("Product of all numbers:", product)
