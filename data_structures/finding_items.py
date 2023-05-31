letters = ["a", "b", "c", "a"]

print(letters.count("a"))  # 2 occurences on list
print(letters.index("a"))  # first position of "a" is index 0

if "d" in letters:  # first we check if "d" is on the list, otherwise we get an error
    print(letters.index("d"))
