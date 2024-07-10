# https://rszalski.github.io/magicmethods/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # Magic method
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(3, 1)
point2 = Point(1, 2)
print(point + point2)
