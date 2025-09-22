import os
import sys

def copyfile(filename1,filename2):
    ret=os.path.exists(filename1)

    if(ret==True):
        print("fil exists in current directory")
        fobj=open(filename1,"r")
        data = fobj.read()
        print("file data is:",data)
        fobj1=open(filename2,"a")

        for line in data:
            fobj1.write(line)

        fobj.close()
        fobj1.close()

    else:
        print("file does not exist in current directory")

    def main():
        if(len(sys.argv)==3):
            copyfile(sys.argv[1],sys.argv[2])

    if __name__=="__main__":
        main()