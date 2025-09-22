from functools import reduce

input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
filtered = list(filter(lambda x: 70 <= x <= 90, input_list))
mapped = list(map(lambda x: x + 10, filtered))
reduced = reduce(lambda x, y: x * y, mapped)

print("Filtered List:", filtered)
print("Mapped List:", mapped)
print("Output of reduce:", reduced)
