def natural(n):
    if n==0:
        return 0
    return n+natural(n-1)
num=int(input("enter the numbers:"))
print("sum of n natural no is :",natural(num))