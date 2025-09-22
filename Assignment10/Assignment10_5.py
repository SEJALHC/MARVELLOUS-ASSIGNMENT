from functools import reduce

def prime(no1):
    primeno = True
    for i in range(2,no1):
        if no1 % i == 0:
            primeno = False
            return False
        
    if primeno :
        return True
    
def multiplication(no1):
    ans = no1 * 2
    return ans

def maximum (no1 , no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    data= []
    print("Enter your number :")
    no1 =int(input())
     
    print("Enter your element :")
    for i in range(no1):
        no = int(input())
        data.append(no)
    print("Input Data :",data)
    
    Fdata = list (filter(prime,data))
    print("List after Filter :",Fdata)
    
    Mdata = list (map(multiplication,Fdata))
    print("List after Map :",Mdata)
    
    Rdata = reduce(maximum,Mdata)
    print("Output of Reduce :",Rdata)

if __name__ == "__main__":
    main()