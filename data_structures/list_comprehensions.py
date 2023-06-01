items = [
    ("Product1", 10),
    ("Product2", 6),
    ("Product3", 15)
]

prices = list(map(lambda item: item[1], items))
print(prices)

prices_comprehensions = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

filtered_comprehensions = [item for item in items if item[1] >= 10]

print("---------------------- comprehensions -------------------------")
print(prices_comprehensions)
print(filtered_comprehensions)
