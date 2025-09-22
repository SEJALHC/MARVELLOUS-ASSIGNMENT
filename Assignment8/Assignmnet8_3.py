import threading

def sumeven(lst):
    total = sum([i for i in lst if i % 2 == 0])
    print("Sum of even numbers:", total)

def sumodd(lst):
    total = sum([i for i in lst if i % 2 != 0])
    print("Sum of odd numbers:", total)

lst = list(map(int, input("Enter list elements separated by space: ").split()))

even_thread = threading.Thread(target=sumeven, args=(lst,))
odd_thread = threading.Thread(target=sumodd, args=(lst,))

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
