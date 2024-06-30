from timeit import timeit

# Cost of Raising Exceptions

CODE1 = """
def calcilate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calcilate_xfactor(-1)
except ValueError as error:
    pass
"""
CODE2 = """
def calcilate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calcilate_xfactor(-1)
if xfactor == None:
    pass
"""
print("first code:", timeit(CODE1, number=10000))
print("second code:", timeit(CODE2, number=10000))
# The first code is slower because raising exceptions is expensive.
