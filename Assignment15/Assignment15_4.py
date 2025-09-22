import os
import sys

def copyfile(filename1,filename2):
    ret=os.path.exists(filename1)
    ret1=os.path.exists(filename2)

    if(ret==True and ret1==True):
        print("files exists in current directory")
        fobj=open(filename1,"r")
        data=fobj.read()
        fobj1=open(filename2,"r")
        data1=fobj1.read()

        if(data==data1):
            print("success")
        else:
            print("failure")

    else:
        print("file does not exist in current directory")


def main():
    if(len(sys.argv)==3):
        copyfile(sys.argv[1],sys.argv[2])


if __name__=="__main__":
    main()

