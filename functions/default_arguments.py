# Default Arguments

# We set the by argument to one
def increment(number, by=1):  # remember to always put the optional parameters at the end
    return number + by


print(increment(2))  # Making the by argument optional
