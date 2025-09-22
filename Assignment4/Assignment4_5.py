from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

input_list = [2, 70, 11, 10, 17, 23, 31, 77]
filtered = list(filter(is_prime, input_list))
mapped = list(map(lambda x: x * 2, filtered))
reduced = reduce(lambda x, y: x if x > y else y, mapped)

print("Filtered List:", filtered)
print("Mapped List:", mapped)
print("Output of reduce:", reduced)
