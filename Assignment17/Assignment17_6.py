import schedule
import time

def task1():
    print("Lunch Time")

def task2():
    print("wrap up work")

def main():
    print("python job scheduler")

    schedule.every().day.at("13:00").do(task1)

    schedule.every().day.at("18:00").do(task2)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()