from sys import getsizeof

values = [x * 2 for x in range(10)]
for x in values:
    print(x)
print("--------------------------------------------")
values = (x * 2 for x in range(10))
print(values)
for x in values:
    print(x)
print("--------------------------------------------")
values = (x * 2 for x in range(1000))
print("gen: ", getsizeof(values))
print("--------------------------------------------")
values = (x * 2 for x in range(100000))
print("gen: ", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("list: ", getsizeof(values))
print("--------------------------------------------")
values = (x * 2 for x in range(100000))
print(len(values))  # we can't have the length of a generator ahead of time
