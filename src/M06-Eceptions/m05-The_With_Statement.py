
try:
    with open("myfile1.txt", "w", encoding="UTF-8") as file, open("myfile2.txt", "w", encoding="UTF-8") as file2:
        file.write("Hello World")
        file2.write("Hello World")

    age = int(input("Enter your age: "))
    xfactor = 10 / age
#  only eecute the firsr except block that matches the exception
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
