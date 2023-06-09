class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# All classes inherit from "object" the object class


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

o = object()
print(issubclass(Mammal, Animal))
print(issubclass(Animal, object))
