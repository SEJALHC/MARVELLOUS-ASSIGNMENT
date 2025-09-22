import threading

def evenfact(n):
    total = 0
    print("Even factors of", n, ":")
    for i in range(2, n+1, 2):
        if n % i == 0:
            print(i)
            total += i
    print("Sum of even factors:", total)

def oddfact(n):
    total = 0
    print("Odd factors of", n, ":")
    for i in range(1, n+1, 2):
        if n % i == 0:
            print(i)
            total += i
    print("Sum of odd factors:", total)

num = int(input("Enter a number: "))

even_thread = threading.Thread(target=evenfact, args=(num,))
odd_thread = threading.Thread(target=oddfact, args=(num,))

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("exit from main")
