def power(n,m):#n=pwr
    if m==0:
        return 1
    return n * power(n,m-1)

pwr=int(input("enter exponent:"))
base=int(input("enter base:"))
print("power:",power(base,pwr))