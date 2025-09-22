def digit(n):
    if n==0:
        return 0
    last=n%10
    rem=n//10
    print(f"addition:{last},remaining:{rem}")
    return last+digit(rem)

num=int(input("enter a number"))
print("sum is:",digit(num))
