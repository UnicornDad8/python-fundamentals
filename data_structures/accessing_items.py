letters = ["a", "b", "c", "d"]
print(letters[0])
print(letters[-1])  # letters[len(letters) + 1]

# modifying an item
letters[1] = "z"
print(letters)

# slicing the list
print(letters[1:3])
print(letters[:])  # copy of the original list
print(letters[::2])  # you added a step to grab only even indexes
numbers = list(range(20))
print(numbers[::2])  # print all even numbers from 0 to 20
print(numbers[::-1])  # this will copy the list and reverse it
