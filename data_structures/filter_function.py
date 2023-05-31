items = [
    ("Product1", 10),
    ("Product2", 6),
    ("Product3", 15)
]

filtered = []
for item in items:
    if (item[1] >= 10):
        filtered.append(item[1])

print(filtered)
print("--------------------------------------------------------")

filtererd_list = list(filter(lambda item: item[1] >= 10, items))
print(filtererd_list)
