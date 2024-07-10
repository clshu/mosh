# Data only calsses
from collections import namedtuple

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(p[0], p[1])

p2 = Point(x=1, y=2)
print(p == p2)

# Named tuple is immutable
# p.x = 3 is not allowed
# p.z = 3 is not allowed

# Named tuple is lightweight

p2 = Point(x=10, y=1)  # This is a new object, reassign x
print(p2)
