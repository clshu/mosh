# https://rszalski.github.io/magicmethods/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # Magic method
        return f"({self.x}, {self.y})"


point = Point(3, 1)
print(point)
print(str(point))
