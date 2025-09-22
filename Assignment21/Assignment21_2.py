import psutil
import sys

def ProcessDisplay(Processname):
    result = False

    for proc in psutil.process_iter(attrs = ['name']):
        if proc.info['name'] == Processname:
            print("The process is running :",Processname)
            result =True
            break
        
    if not result:
        print("The process is not running :",Processname)
            
            
    
def main():
    
    if(len(sys.argv) == 2):
        ProcessDisplay(sys.argv[1])
        
        

if __name__ == "__main__":
    main()