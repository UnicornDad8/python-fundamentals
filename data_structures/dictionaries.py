point = {"x": 1, "y": 2}

# here are some convert functions
list()
tuple()
set()
dict()

point = dict(x=1, y=2)
print(point["x"])

point["x"] = 7
print(point["x"])

point["z"] = 5
print(point)

if "a" in point:
    print(point["a"])

print(point.get("a", 0))

del point["x"]
print(point)

for key in point:
    print(key, point[key])
print("-------------------------------------------------------------")
for key, value in point.items():
    print(key, value)
