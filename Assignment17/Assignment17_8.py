import schedule
import time

def mailchecking():
    print("checking mail.......")

def main():
    schedule.every(10).seconds.do(mailchecking)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()