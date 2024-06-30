from array import array

# typecode: 'i' (signed integer)
# https://docs.python.org/3/library/array.html

numbers = array('i', [1, 2, 3, 4, 5])

numbers.append(6)
numbers.insert(0, 0)
print(numbers)
numbers.pop()
print(numbers)
