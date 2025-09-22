import schedule
import time 
import datetime

def myschedule():
    print("the current date and ime :",datetime.datetime.now())

def main():
    print("the current date and rime is :",datetime.datetime.now())

    schedule.every(1).minutes.do(myschedule)

    while True:
        schedule.run_pendig()
        time.sleep(1)

if __name__=="__main__":
    main()