def num(number):

    if number==0:
        print("zero")

    if number>0:
        print("positive number")

    else:print("negative no")

number = int(input("Enter a number: "))

# Call the function and print result
result =num(number)
print(f"The number {number} is {result}")

