#       Find the lowest number
#   This program will ask for three (3) numbers.
#   It will then find the lowest number.

#Step 1: Ask for user inputs and assign them to values.
print("Input three (3) numbers and the program will find the lowest number.\n")
def userNumbers():
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    c = int(input("Input the third number: "))
    return a, b, c
a, b, c = userNumbers()

#Step 2: Set up the conditions to find the lowest number.
def findLowest():
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c