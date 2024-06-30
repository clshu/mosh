
items = [('Product1', 10), ('Product2', 9), ('Product3', 12)]

# [expression for item in items]

prices = list(map(lambda item: item[1], items))
prices1 = [item[1] for item in items]
print(prices1)
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered1 = [item for item in items if item[1] >= 10]
print(filtered1)
