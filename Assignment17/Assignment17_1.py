import schedule
import time

def main():
    print("jay ganesh")


    schedule.every(2).seconds.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()
