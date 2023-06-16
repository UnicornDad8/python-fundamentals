"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(id(p1))
print(id(p2))
"""
# We use namedtuples when we only have data and no methods in the class like
# the example of the Point class with x and y attributes
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
print(id(p1))
print(id(p2))

# Remeber we are using tuples so we can't modify the x or y values once
# we set them

# p1.x = 10 # This line will throw an error, uncoment to read the error
# p1 = Point(x=10, y=2) # if you actually want to modify x you use this line
