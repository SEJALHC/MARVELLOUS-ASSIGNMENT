import os
import sys

def CopyFile(filename1,filename2):
    
   ret = os.path.exists(filename1)
   
   if(ret == True):
       print("The File is exists in current directory")
       fobj = open(filename1,"r")
       data = fobj.read()
       print ("File Data is : ",data)
       fobj1 = open(filename2,"a")
       
       for line in data:
           fobj1.write(line)
       fobj.close()
       fobj1.close()
   else:
       print("The File is not exists in current directory")
       

def main():
    if(len(sys.argv) == 3):
        CopyFile(sys.argv[1],sys.argv[2])
        
        
if __name__ == "__main__":
    main()