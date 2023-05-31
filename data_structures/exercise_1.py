'''
Given an array of integers, find the pair of adjacent elements that 
has the largest product and return that product.

Example:

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
'''


def solution(input_array):
    sum = []

    for i in range(len(input_array) - 1):
        sum.append(input_array[i] * input_array[i + 1])

    return max(sum)


print(solution([3, 6, -2, -5, 7, 3]))
