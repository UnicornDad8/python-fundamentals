chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
'''
first = chars[0]
second = chars[1]
third = chars[2]
-----------------------------
other = chars[3:-1]
last = chars[-1]
'''
first, second, third, *other, last = chars  # this line is equivalent to the comment above

print(first)
print(second)
print(third)
print(chars[3:-1])
print("-----------------------------------------------------")
print(other)
print(last)
