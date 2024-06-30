
try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age
#  only eecute the firsr except block that matches the exception
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
