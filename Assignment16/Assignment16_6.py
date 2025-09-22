def display(file1,file2):

    fobj = open(file1,'r')
    data =fobj.read()
    fobj1 =open(file2,'a')

    for line in data:
        fobj1.write(line)
    fobj.close()
    fobj.close()

def main():
    print("enter your filename:")
    file1=input()


    print("enter your copy filename:")
    file2 =input()

    display(file1,file2)
if __name__=="__main__":
    main()