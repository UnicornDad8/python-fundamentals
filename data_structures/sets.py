# Set is unordered collection of unique items, we canot have duplicates
# and this objects are in secuence, so we can't access them using
# an index like lists, but we can check the existence of an item in the set

numbers = [1, 1, 1, 2, 2, 3, 4, 3, 3]
uniques = set(numbers)

print(uniques)

second = {1, 5}
second.add(6)
print(second)
second.remove(6)
print(second)
print(len(second))

first = uniques
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")
