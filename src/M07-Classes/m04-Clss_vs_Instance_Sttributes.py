class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(3, 1)
print(type(point))
print(isinstance(point, Point))
point.draw()
print(Point.default_color)
print(point.default_color)

Point.default_color = "yellow"
print(Point.default_color)
print(point.default_color)
