# a tuple is basically a read only list

point = (1, 2)
print(point)
print(type(point))

# concatenate tuple
point = (1, 2) + (3, 4)
print(point)

point = (1, 2) * 3
print(point)

letters = tuple("abc")
print(letters)

numbers = tuple([1, 2, 3])
print(numbers)

print(numbers[0])
print(numbers[1: 3])

# unpack tuple
x, y, z = numbers
print(x, y, z)

if "b" in letters:
    print("exist")

# we can't add, remove or modify tuples
# try the line below, uncomment and run it, it should throw an error
# numbers[0] = 13
print(numbers[0])
