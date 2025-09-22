from functools import reduce

def compare(no):
    if (no >= 70 and no <= 90):
     return no
        
def increase(no):
    ans = no + 10
    return ans
    
def product(no1,no2):
    ans = no1 * no2
    return ans

def main():
    data= [4,34,36,76,68,24,89,23,86,90,45,70]

    print("Input Data :",data)
    
    Fdata = list (filter(compare,data))
    print("List after Filter :",Fdata)
    
    Mdata = list (map(increase,Fdata))
    print("List after Map :",Mdata)
    
    Rdata = reduce(product,Mdata)
    print("List after Reduce :",Rdata)

if __name__ == "__main__":
    main()