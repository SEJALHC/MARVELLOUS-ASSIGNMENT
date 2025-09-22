import time
import threading
from multiprocessing import Process


def sum():
    total = 0
    for i in range(1, 10000001):
        total += i
    print("Sum is:", total)

start = time.time()
sum()
print("Normal time:", time.time() - start)
start = time.time()
t = threading.Thread(target=sum)
t.start()
t.join()
print("Threading time:", time.time() - start)


start = time.time()
p = Process(target=sum)
p.start()
p.join()
print("Multiprocessing time:", time.time() - start)
