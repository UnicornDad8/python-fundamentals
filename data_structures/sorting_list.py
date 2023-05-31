numbers = [3, 51, 2, 8, 6]


print(sorted(numbers))  # this does not modify the original list
print(numbers)
print(sorted(numbers, reverse=True))
print("---------------------------------------------")
numbers.sort()
print(numbers)

# to sort in descending order
numbers.sort(reverse=True)
print(numbers)
print("---------------------------------------------")

items = [
    ("Product1", 10),
    ("Product2", 6),
    ("Product3", 15)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
