class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x  # x and y are instance attributes
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"  # class level attributes are shared across
# all instances of a class

point1 = Point(1, 2)
print(point1.default_color)
print(Point.default_color)
point1.draw()

point2 = Point(3, -1)
print(point2.default_color)
point2.draw()
