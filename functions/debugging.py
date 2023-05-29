'''
Fist you press "Fn + F9" to add a bearkpoint, you do it
on line 6, then you press "Fn + F10" to jump to next line
then you can also stop the execution with "shift + F11" or
pressing the square stop button, you can always have more than
one breakpoint
'''


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(2, 3, 4, 5))
