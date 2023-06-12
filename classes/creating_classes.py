# Class: a blueprint for creating new objects
# Object: is an instance of a class

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
