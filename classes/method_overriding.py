class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # if we don't add this line to the mammal constructor
        # all the code in this constructor would replace the animal constructor
        # but now that we added that line we can extend the Animal's constructor
        # and we still have access to the "age" variable
        print("Mammal constructor")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
