import threading

def print_even():
    for i in range(2, 21, 2):  
        print(i)

def print_odd():
    for i in range(1, 20, 2):  
        print(i)


t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)


t1.start()
t2.start()


t1.join()
t2.join()
