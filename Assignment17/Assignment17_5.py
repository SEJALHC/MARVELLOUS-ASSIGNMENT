import schedule
import time
import os
import datetime

def Myschedule():
    data=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fobj=open("Marvellous.txt",'a')
    fobj.write(data+"\n")
    print(data)

def main():
    print("pythn jb scheduler")

    schedule.every(5).seconds.do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()