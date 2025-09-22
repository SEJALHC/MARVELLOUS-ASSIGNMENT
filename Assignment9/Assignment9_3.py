from multiprocessing import Pool
import math

def factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))

    with Pool() as pool:
        results = pool.map(factorial, numbers)

    for num, fact in zip(numbers, results):
        print(f"Factorial of {num} is {fact}")
