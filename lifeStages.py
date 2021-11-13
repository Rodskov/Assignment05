#       Life Stages 
#   This program will ask for your age
#   and display the life stage.

#Step 1: Show the user the life stages of a person, then ask for their age.
def showLifeStages():
    print("The life stages of a person are:")
    print("Ages 0-12: Kid")
    print("Ages 13-17: Teen")
    print("Age 18: Debut")
    print("Ages 19+: Adult")

def userAsk():
    age = int(input("What is your age?: "))
    return age

showLifeStages()
age = userAsk()