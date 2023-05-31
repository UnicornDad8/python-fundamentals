items = [
    ("Product1", 10),
    ("Product2", 6),
    ("Product3", 15)
]

prices = []
for item in items:
    prices.append(item[1])

sorted_prices = sorted(prices)
print(sorted_prices)
print("------------------------------------------------------")

map_iterable = map(lambda item: item[1], items)
sorted_map_prices = sorted(map_iterable)

for item in sorted_map_prices:
    print(item)
print("------------------------------------------------------")

list_of_prices = list(map(lambda item: item[1], items))
print(list_of_prices)
