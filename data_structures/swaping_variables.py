x = 10
y = 11

# to swap variables we need a third variable "z"
z = x
x = y
y = z

print("x: ", x)
print("y: ", y)
print("--------------------------------------------------")

a = 2
b = 5

# but we have a new way to swap in python with only one line of code
a, b = b, a
print("a: ", a)
print("b: ", b)
