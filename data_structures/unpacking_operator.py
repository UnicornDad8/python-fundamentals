# with the unpacking operator we have to prefix our variable with an asterisc
numbers = [1, 2, 3]
print(numbers)
print(*numbers)  # This is similar to the spread operator in JavaScript
print("-------------------------------------------------")
values = list(range(5))
print(values)

values = [*range(5)]
print(values)

booleans_list = [False, False, True, False]
values = [*range(5), *"Hello world", 1.4, " ", *booleans_list]
print(values)

print("-------------------------------------------------")
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)  # note that the value of x is 10, because it was the last value taken
