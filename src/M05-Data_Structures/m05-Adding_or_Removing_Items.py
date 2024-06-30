letters = ['a', 'b', 'c', 'd']

# Add
letters.append('e')
letters.insert(0, '-')
print(letters)

# Remove
letters.pop()
print(letters)
letters.pop(0)
print(letters)
letters.remove('b')
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters)
