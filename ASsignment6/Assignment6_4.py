# Accept a number from the user
num = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Calculate factorial using for loop
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")
