def num(no1):
    fobj=open("num.txt","a")
    for i in range(1,no1+1):
        fobj.write(str(i)+'\n')

    fobj.close()

def main():
    print("entter ur input:")
    no1=int(input())
    num=(no1)

if __name__=="__main__":
    main()