try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("Age can't be zero.")
else:
    print(f"you are {age} years old")

print("--------------------------------------------------------")
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print(f"you are {age} years old")
