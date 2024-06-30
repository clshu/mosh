from sys import getsizeof

values = (x for x in range(10))

print(values)  # <generator object <genexpr> at 0x0000021D3D3D3C80>
for x in values:
    print(x)

values = (x for x in range(10))
print(getsizeof(values))  # 200 on my computer
print(getsizeof(list(values)))  # 184, small for now
values = (x for x in range(100000))
print(getsizeof(values))  # 200, same as range(10), a fixed value
print(getsizeof(list(values)))  # 800984, very large
