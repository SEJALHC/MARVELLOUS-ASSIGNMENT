def Num(number):
    
    if number%5==0:
        return True
    else:
        return False
    
number=int(input())
result=Num(number)
print(f"Is {number} divisible by 5? {result}")