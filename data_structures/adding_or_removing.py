letters = ["a", "b", "c"]

# Add at the end of the list
letters.append("d")
print(letters)

# Add an item at a given index
letters.insert(0, "-")
print(letters)

# Remove at the end of the list
letters.pop()
print(letters)

# Remove item at a given index
letters.pop(2)
print(letters)

# Remove the first occurence of the given value
letters.remove("a")
print(letters)

# with delete we can remove a single item or a set of items
del letters[0:2]
print(letters)

# this will remove all items on the list
letters.clear()
print(letters)
