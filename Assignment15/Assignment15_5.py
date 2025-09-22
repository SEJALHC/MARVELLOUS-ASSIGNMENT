import os 
import sys

def copyfile(filename1,data):
    ret=os.path.exists(filename1)

    if(ret==True):
        print("file exist in directory")
        fobj=open(filename1,"r")
        content=fobj.read()
        print("freuency of string is :",content.count(data))

        fobj.close()

    else:
        print("this file doesnt exist")

def main():
    if(len(sys.argv)==3):
        copyfile(sys.argv[1],sys.argv[2])



if __name__=="__main__":
    main()

        