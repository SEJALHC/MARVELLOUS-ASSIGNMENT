import os
def fileexists(filename):
    check=os.path.exists(filename)

    if(check== True):
        print("file exists in directory")
        fobj=open(filename,"r")
        data=fobj.read()
        print("data from file",data)

        fobj.close()

    else:
        print("nosuch file in directory")

def main():
    print("enter file name:")
    filename=input()

    fileexists(filename)

if __name__=="__main__":
    main()