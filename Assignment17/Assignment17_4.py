import schedule
import time

def Myschedule():
    print("Namskar--------")

def main():
    print("python job schedular")

    schedule.every().day.at("09:00").do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
    