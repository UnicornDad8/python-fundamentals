class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


# This is an example of multiple inheritance or inheritance abuse
# A Chicken is a bird that is correct but a Chicken can't fly
class Chicken(Bird):
    pass


c = Chicken()
print(c.fly())
