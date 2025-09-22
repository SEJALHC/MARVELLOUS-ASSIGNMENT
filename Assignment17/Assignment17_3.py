import schedule
import time

def Myschedule():
    print("do coding-----")

def main():
    print("python job scheduler")

    schedule.every(30).minutes.do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()