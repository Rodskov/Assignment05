#       PUP Grading System
#   This program will ask for grade percentage.
#   It will then display the equivalent
#   grade/mark and description.

#Step 1: Show the user the equivalent grade marks and description
def gradeTable():
    print(" Grade/Mark | Percentage/Equivalent |   Description  ")
    print("    1.0     |         97-100        |    Excellent   ")
    print("    1.25    |          94-96        |    Excellent   ")
    print("    1.5     |          91-93        |    Very Good   ")
    print("    1.75    |          88-90        |    Very Good   ")
    print("    2.0     |          85-87        |       Good     ")
    print("    2.25    |          82-84        |       Good     ")
    print("    2.5     |          79-81        |   Satisfactory ")
    print("    2.75    |          76-78        |   Satisfactory ")
    print("    3.0     |           75          |      Passing   ")
    print("    5.0     |          65-74        |      Failure   ")
    print("    Inc.    |                       |    Incomplete  ")
    print("     W      |                       |     Withdrawn  ")
    print("     D      |                       |      Dropped   \n")

#Step 2: Let the user input their grade.
def gradeInput():
    gradeInput = float(input("Input Grade: "))
    return gradeInput

#Step 3: Set up display conditions for equivalence
def equiGrade():
    if gUser >= 97 and gUser <= 100:
        print("Grade/Mark: 1.0")
    elif gUser >= 94 and gUser <= 96:
        print("Grade/Mark: 1.25")
    elif gUser >= 91 and gUser <= 93:
        print("Grade/Mark: 1.5")
    elif gUser >= 88 and gUser <= 90:
        print("Grade/Mark: 1.75")
    elif gUser >= 85 and gUser <= 87:
        print("Grade/Mark: 2.0")
    elif gUser >= 82 and gUser <= 84:
        print("Grade/Mark: 2.25")
    elif gUser >= 79 and gUser <= 81:
        print("Grade/Mark: 2.5")
    elif gUser >= 76 and gUser <= 78:
        print("Grade/Mark: 2.75")
    elif gUser == 75:
        print("Grade/Mark: 3.0")
    else:
        pass
gradeTable()
gUser = gradeInput()
equiGrade()