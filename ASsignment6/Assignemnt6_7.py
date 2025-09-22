
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print("The largest number is:", largest)
