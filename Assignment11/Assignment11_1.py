def num(n,i=1):
    if i>n:
        return
    print(i, end=" ")
    num(n,i+1)


number=int(input("enter the number"))
print("numbers are:",num(number))