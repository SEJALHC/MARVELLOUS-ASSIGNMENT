from functools import reduce

even = lambda A : A % 2 == 0

square = lambda A : A **2

addition = lambda A , B : A + B

def main():
    data= []
    print("Enter your number :")
    no1 =int(input())
     
    print("Enter your element :")
    for i in range(no1):
        no = int(input())
        data.append(no)
    print("Input Data :",data)
    
    Fdata = list (filter(even,data))
    print("List after Filter :",Fdata)
    
    Mdata = list (map(square,Fdata))
    print("List after Map :",Mdata)
    
    Rdata = reduce(addition,Mdata)
    print("Output of Reduce :",Rdata)

if __name__ == "__main__":
    main()