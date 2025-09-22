import hashlib
import os

def Calculatechecksum(path,blocksize =1024):
    fobj = open(path,'rb')
    hobj = hashlib.md5()
    
    buffer = fobj.read(blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)
    fobj.close()
    
    return hobj.hexdigest()

def DirectoryWatcher(Directory):
    
    flag = os.path.abspath(Directory)
    
    if(flag == False):
        Directory = os.path.abspath(Directory)
        
    flag = os.path.exists(Directory)
    
    if(flag == False):
        print("The path is invaild")
        exit()
        
    flag = os.path.isdir(Directory)
    if (flag == False):
        print("Path is vaild but the target is not a directory")
        exit()
    
    for FolderName, SubFolderNames, FilesNames in os.walk(Directory):
           for fname in FilesNames :
               fname = os.path.join(FolderName,fname)
               checksum = Calculatechecksum(fname)
               print("File Name :",fname)
               print("checksum :",checksum)
               print()
        
        
def main():
    print("Enter your Directory name :")
    Directoryname = input()
    
    ret = DirectoryWatcher(Directoryname)

if __name__ == "__main__":
    main()