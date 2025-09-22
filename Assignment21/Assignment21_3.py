import psutil
import os
import time
import sys

def Createlog(Foldername):
    if not os.path.exists(Foldername):
        os.mkdir(Foldername)
        
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","")
    timestamp = timestamp.replace("/","")
    
    Filename = os.path.join(Foldername,"Marvellous%s.log"%(timestamp))
    
    fobj = open(Filename,"w")
    
    broder = "-"*80
    fobj.write(broder)
    fobj.write("\n\t\tMarvellous infosystems Process log\n")
    fobj.write("\t\tlog file is created at:"+time.ctime()+"\n")
    fobj.write(broder)
    Data = ProcessScan()
    
    for value in Data:
        fobj.write("%s \n\n" %value)
    fobj.write(broder)
    fobj.close()
    
def ProcessScan():

    listprocess = []    
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024*1024)
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess) :
            pass
    
    return listprocess 

def main():
    if(len(sys.argv) == 2):
        Createlog(sys.argv[1])
    
if __name__ =="__main__":
    main()