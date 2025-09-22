import threading
import time

def print_num(name):
    for i in range(1, 6):
        print(f"{name} prints: {i}")
        time.sleep(1)


t1 = threading.Thread(target=print_num, args=("Thread 1",))
t2 = threading.Thread(target=print_num, args=("Thread 2",))
t3 = threading.Thread(target=print_num, args=("Thread 3",))

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
