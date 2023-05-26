'''
Write a program to display the even numbers from 1 to ten.
hint: use range(1, 10)
and then print a message saying how many even numbers you have.
-------------- output should be ----------------------------------
> 2
> 4
> 6
> 8
> we have 4 even numbers
'''
count = 0
for number in range(1, 10):
    if (number % 2 == 0):
        count += 1
        print(number)
else:
    print(f"we have {count} even numbers")
