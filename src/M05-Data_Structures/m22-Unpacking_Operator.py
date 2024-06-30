values = list(range(5))
print(values)  #
# Similar to spread operator in JavaScript
# ...range(5)
print(*range(5))
values = [*range(5), *"Hello"]

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)  # [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']

# Unpacking dictionaries  (Python 3.5+)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
# duplicate key, the last key will be used
print(combined)  # {'x': 10, 'y': 2, 'z': 1}
