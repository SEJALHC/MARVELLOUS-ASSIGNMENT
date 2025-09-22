def display(file1):

    fobj=open(file1,"r")
    cnt=0

    for line in fobj.readlines():
        if 5<=len(line.split()):
            line = line.replace("\n","")
            print(line)

def main():
    print("enter your filename:")
    file1=input()

    display(file1)

if __name__=="__main__":
    main()