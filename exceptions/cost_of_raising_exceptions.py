# if we don't need to raise exceptions then we can just use an if statement
# sometimes raising exceptions can be costly so we only raise exceptions
# when we really have to.
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be zero or less than zero")
    return 10 / age


try:
    calculate_xfactor(-5)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-5)
if xfactor == None:
  pass
"""
print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
