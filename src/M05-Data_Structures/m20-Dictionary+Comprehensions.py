
values = []
for x in range(5):
    values.append(x * 2)

# [expression for item in iterable if condition]
values = [x * 2 for x in range(5)]
print(values)
values_set = {x * 2 for x in range(5)}
print(values_set)

values_dict = {}
for x in range(5):
    values_dict[x] = x * 2

# [key_expression: value_expression for item in iterable]
values_dict = {x: x * 2 for x in range(5)}
print(values_dict)
