class Point:
    def __init__(self, x, y):  # The methods with double underscore "__"
        self.x = x  # are the magic methods
        self.y = y

    def __str__(self):  # This is another magic method besides __init__
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
