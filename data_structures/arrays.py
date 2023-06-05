from array import array

numbers = array("i", [1, 2, 3])
# with array we have all the same behavior and methods from lists
# but with one difference, which is that all items must be of the
# same type, so if we have a list of integers we can only use integers

# trying to replace a float will throw an error
numbers[0] = 1.3

# also we only use arrays instead of lists when we encouter
# performance problems, otherwise we use lists
