list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))

# we can work not only with lists but with any iterable
# like a string "abc"
print(list(zip("abc", list1, list2)))
