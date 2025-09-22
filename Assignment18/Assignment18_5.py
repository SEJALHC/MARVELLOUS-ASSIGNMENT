import os
import sys

def CopyFile(filename1,Data):
    
   ret = os.path.exists(filename1)
   
   if(ret == True):
       print("The File is exists in current directory")
       fobj = open(filename1,"r")
       Content = fobj.read()
       print("Frequency of string :",Content.count(Data))
       
       fobj.close()
   else:
       print("The File is not exists in current directory")
       

def main():
    if(len(sys.argv) == 3):
        CopyFile(sys.argv[1],sys.argv[2])
        
        
if __name__ == "__main__":
    main()