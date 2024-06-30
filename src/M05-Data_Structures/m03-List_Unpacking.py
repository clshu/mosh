numbers = [1, 2, 3]
first, second, third = numbers
print(first)
more = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other = more
print(other)
first, *other, last = more
print(other)
print(first, last)
