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
    gradeInput = float(input("Input Grade: \nEnter:\n[1] if Incomplete\n[2] if Withdrawn\n[3] if Dropped\n\n"))
    return gradeInput

#Step 3: Set up display conditions for marks and equivalence.
def equiGrade():
    if gUser >= 97 and gUser <= 100:
        print(f"Input Grade: {gUser}\nGrade/Mark: 1.0\nDescription: Excellent")
    elif gUser >= 94 and gUser <= 96:
        print(f"Input Grade: {gUser}\nGrade/Mark: 1.25\nDescription: Excellent")
    elif gUser >= 91 and gUser <= 93:
        print(f"Input Grade: {gUser}\nGrade/Mark: 1.5\nDescription: Very Good")
    elif gUser >= 88 and gUser <= 90:
        print(f"Input Grade: {gUser}\nGrade/Mark: 1.75\nDescription: Very Good")
    elif gUser >= 85 and gUser <= 87:
        print(f"Input Grade: {gUser}\nGrade/Mark: 2.0\nDescription: Good")
    elif gUser >= 82 and gUser <= 84:
        print(f"Input Grade: {gUser}\nGrade/Mark: 2.25\nDescription: Good")
    elif gUser >= 79 and gUser <= 81:
        print(f"Input Grade: {gUser}\nGrade/Mark: 2.5\nDescription: Satisfactory")
    elif gUser >= 76 and gUser <= 78:
        print(f"Input Grade: {gUser}\nGrade/Mark: 2.75\nDescription: Satisfactory")
    elif gUser == 75:
        print(f"Input Grade: {gUser}\nGrade/Mark: 3.0\nDescription: Passing")
    elif gUser >= 65 and gUser <= 74:
        print(f"Input Grade: {gUser}\nGrade/Mark: 5.0\nDescription: Failure")
    else:
        pass

gradeTable()
gUser = gradeInput()

#Step 4: Consider the [1],[2], and [3] options during the user input
def otherOutputs():
    if gUser == 1:
        print("Grade/Mark: Unavailable\nDescription: Incomplete")
    elif gUser == 2:
        print("Grade/Mark: Unavailable\nDescription: Withdrawn")
    elif gUser == 3:
        print("Grade/Mark: Unavailable\nDescription: Dropped")
    else:
        pass

equiGrade()
otherOutputs()