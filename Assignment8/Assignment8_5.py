import threading

def up():
    for i in range(1, 51):
        print(i)

def down():
    for i in range(50, 0, -1):
        print(i)

t1 = threading.Thread(target=up)
t2 = threading.Thread(target=down)

t1.start()
t1.join()  
t2.start()
t2.join()
