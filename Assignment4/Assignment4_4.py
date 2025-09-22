from functools import reduce

input_list = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
filtered = list(filter(lambda x: x % 2 == 0, input_list))
mapped = list(map(lambda x: x ** 2, filtered))
reduced = reduce(lambda x, y: x + y, mapped)

print("Filtered List:", filtered)
print("Mapped List:", mapped)
print("Output of reduce:", reduced)
