"""
class Employee:
    def greet(self):
        print("Employee greet")


class Person:
    def greet(self):
        print("Person greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet() # uses the greet of the Employee because is declared first
"""
# The first example was a bad example of multiple inheritance, but
# the example of the flying fish is a good example of multiple inheritance
# because the class Flyer and the class Fish don't have anything in common
# and a Flying Fish is a fish who can fly and swim


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
