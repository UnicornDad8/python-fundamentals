'''
Write a program that prints the numbers from 1 to 20, but 
for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
'''


def fizzBuzz(input):
    if input % 15 == 0:  # if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return input


print("-------------------------------------------------")
print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(7))
print(fizzBuzz(11))
print("-------------------------------------------------")
