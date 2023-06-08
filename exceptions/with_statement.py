# if we use the with statement we don't need a finally clause
# because the file will close after execution by default
try:
    with open("cleaning_up.py") as file:
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print(f"you are {age} years old")
