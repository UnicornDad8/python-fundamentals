# Strings in Python

# multiline string
message = """Hi John, this is Ceci...
I want to teach programming to other students.
I am working hard to be a teacher
"""
print(message)

course = "Programming"
# use len function to store the length of the string
print(len(course))
# use the 'f' before quotes to create a template literal
print(f"the word: '{course}', has {len(course)} characters")
print(f"the fisrt character of the word '{course}' is '{course[0]}'")
print(course[-1])
# slicing a string
print(course[1:4])  # rog
