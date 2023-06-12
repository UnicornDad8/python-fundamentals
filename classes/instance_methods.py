class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # This is called a decorator
    def zero(cls):  # This is a class method
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()  # This is a factory method => Point(0, 0)
point.draw()  # This is an instance method because
# is using an instantiated object to be called
