def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(is_prime, numbers))


nums = list(map(int, input("Enter numbers separated by space: ").split()))
primes = filter_primes(nums)
print("Prime numbers:", primes)
