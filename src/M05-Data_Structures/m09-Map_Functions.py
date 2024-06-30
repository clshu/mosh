
items = [('Product1', 10), ('Product2', 9), ('Product3', 12)]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

# map() function returns a map object which is an iterator

prices = list(map(lambda item: item[1], items))

print(prices)
