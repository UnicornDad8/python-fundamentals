# The asterisc before the plural variable grabs all arguments you pass to the function

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
