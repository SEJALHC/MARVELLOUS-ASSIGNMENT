import os
import hashlib
import time
import sys

def Calculatechecksum(path,size =1024):
    
    fobj = open(path,'rb')
    hobj = hashlib.md5()
    
    buffer = fobj.read(size)
    if(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(size)
    
    fobj.close()
    
    return hobj.hexdigest()

def Logfile(result):
    
    filename = "Log.txt"
        
    fobj = open(filename,"w")
        
    Broder = "_"*54
        
    fobj.write(Broder+"\n")
    fobj.write("This is a log file of Marvellous Automation Script"+"\n")
    fobj.write(Broder+"\n")
    temp = []
        
    for value in result.values():
            if len(value)>1:
                temp.append(value)
                fobj.write(" ".join(value))
    
    fobj.close()


def FindDuplicates(Directoryname):
    flag = os.path.abspath(Directoryname)
    
    if(flag == False):
        Directoryname = os.path.abspath(Directoryname)
    flag = os.path.exists(Directoryname)
    
    if(flag == False):
        print("Path is invaild")
        exit()
        
    flag = os.path.isdir(Directoryname)
    if (flag == False):
        print("Path is vaild but the target is not a directory")
        exit()
        
    Duplicates = {}
     
    for Foldername , SubFolderName, FilesNames in os.walk(Directoryname):
        for fname in FilesNames:
            file_path = os.path.join(Foldername,fname)
            check = Calculatechecksum(file_path)
            
            if(check in Duplicates):
                Duplicates[check].append(fname)
            else:
                Duplicates[check] = [fname]
    return Duplicates

def main():
    if(len(sys.argv) ==2):
        result = FindDuplicates(sys.argv[1])
        Logfile(result)
        
        
        
if __name__ =="__main__":
    main()