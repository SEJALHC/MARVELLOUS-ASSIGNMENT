def star(row,n=1):
    if n>row:
        return
    print("*"*n)
    star(row,n+1)
num=int(input("enter a num"))
print(star(num))

