import os
import sys

def CopyFile(filename1,filename2):
    
   ret = os.path.exists(filename1)
   ret1 = os.path.exists(filename2)
   
   if(ret == True and ret1 == True):
       print("The File is exists in current directory")
       fobj = open(filename1,"r")
       data = fobj.read()
       fobj1 = open(filename2,"r")
       data1 = fobj1.read()
       
       if(data == data1):
           print("Success")
       else:
           print("Failure")
    
       fobj.close()
       fobj1.close()
   else:
       print("The File is not exists in current directory")
       

def main():
    if(len(sys.argv) == 3):
        CopyFile(sys.argv[1],sys.argv[2])
        
        
if __name__ == "__main__":
    main()