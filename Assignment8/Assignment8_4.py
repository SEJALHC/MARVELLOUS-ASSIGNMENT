import threading

def small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Lowercase letters:", count)
    print("Thread ID:", threading.get_ident(), " Name:", threading.current_thread().name)

def capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Uppercase letters:", count)
    print("Thread ID:", threading.get_ident(), " Name:", threading.current_thread().name)

def digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Digits:", count)
    print("Thread ID:", threading.get_ident(), "Name:", threading.current_thread().name)


input_str = input("Enter a string: ")
t1 = threading.Thread(target=small, args=(input_str,), name="SmallThread")
t2 = threading.Thread(target=capital, args=(input_str,), name="CapitalThread")
t3 = threading.Thread(target=digits, args=(input_str,), name="DigitThread")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
