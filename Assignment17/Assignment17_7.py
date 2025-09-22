import schedule
import time
import datetime
import os 

def Backup():
    data=datetime.datetime.now().strftime('%Y-%m-%-d %H:%M:%S')
    fobj= open("backup_log.txt",'a')
    fobj.write("backup log entry isb :",data+"\n")
    print(data)

def main():
    print("python job scheduler")

    schedule.every(1).hours.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()