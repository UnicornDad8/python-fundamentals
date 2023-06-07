try:
    file = open("cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print(f"you are {age} years old")
finally:
    file.close()
