# https://rszalski.github.io/magicmethods/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __gt__(self, other) -> bool:
        return self.x > other.x and self.y > other.y


point = Point(3, 1)
other_point = Point(3, 1)
print(point == other_point)
point = Point(10, 20)
other_point = Point(1, 2)
print(point > other_point)
point, other_point = other_point, point
print(point < other_point)
