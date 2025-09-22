from multiprocessing import Process

def square(nums):
    for n in nums:
        print(f"Square of {n} is {n * n}")

if __name__ == "__main__":
    input = input("Enter numbers separated by space: ")
    numbers = list(map(int, input.split()))

    p = Process(target=square, args=(numbers,))
    p.start()
    p.join()
