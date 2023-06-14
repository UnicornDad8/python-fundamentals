class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent or Base class
# Mammal: Child or Sub class


class Mammal(Animal):
    def walk(self):
        print("walk")

# Another Sub class


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print("-----------------------------------------------")

f = Fish()
f.eat()
print(f.age)
