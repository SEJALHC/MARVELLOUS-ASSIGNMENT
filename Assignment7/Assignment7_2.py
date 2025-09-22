
input_str = input("Enter integers separated by spaces: ")
numbers = list(map(int, input_str.split()))

doubled = list(map(lambda x: x * 2, numbers))

print("Original list:", numbers)
print("Doubled list: ", doubled)
