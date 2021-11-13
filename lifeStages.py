#       Life Stages 
#   This program will ask for your age
#   and display the life stage.

#Step 1: Show the user the life stages of a person, then ask for their age.
def showLifeStages():
    print("The life stages of a person are:")
    print("Ages 0-12: Kid")
    print("Ages 13-17: Teen")
    print("Age 18: Debut")
    print("Ages 19+: Adult\n")

def userAsk():
    global age
    age = int(input("What is your age?: "))
    return age

showLifeStages()
age = userAsk()

#Step 2: Prepare the conditions and show the output.
def evalAge(age):
    if age <= 12:
        print(f"You are {age} years old and a kid! Have fun!")
    elif age >= 13 and age <= 17:
        print(f"You are {age} years old and a teen! Good luck!")
    elif age == 18:
        print(f"You are {age} years old! Congratulations on your debut!")
    else:
        print(f"You are {age} years old and an adult! Good luck on your responsibilities!")
evalAge(age)