
input_str = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_str.split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original list:", numbers)
print("Even numbers:  ", even_numbers)
