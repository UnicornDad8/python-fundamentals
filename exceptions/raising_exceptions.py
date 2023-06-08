def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be zero or less than zero")
    return 10 / age


try:
    calculate_xfactor(-5)
except ValueError as error:
    print(error)
