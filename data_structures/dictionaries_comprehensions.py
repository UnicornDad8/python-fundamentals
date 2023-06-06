print("--------------------- comprehesion lists ----------------------")
values_list = []
for x in range(5):
    values_list.append(x*2)

values_list = [x * 2 for x in range(5)]
print(values_list)

print("--------------------- comprehesion dictionaries ----------------------")
values_dictionary = {x * 2 for x in range(5)}
print(values_dictionary)

values_dictionary = {}
for x in range(5):
    values_dictionary[x] = x * 2

values_dictionary = {x: x * 2 for x in range(5)}
print(values_dictionary)

print("--------------------- comprehesion tuples ----------------------")
values_tuple = (x * 2 for x in range(5))
print(values_tuple)  # we don't get a tuple but a generator expression
