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
    print("     D      |                       |      Dropped   ")
print(gradeTable())