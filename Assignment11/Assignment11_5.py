def zero(n):
    if n==0:
        return 0
    if n % 10 ==0:
        return 1+ zero(n//10)
    else:
        return zero(n//10)
num=int(input())
print("zeros are:",zero(num))