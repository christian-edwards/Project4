import random


def rollerWith(sides):
    try:
        if sides < 2:
            raise ValueError
    except ValueError:
        print("ERROR Invalid entry: Must be an integer greater than 1.")
        return
    randomNumber = random.randrange(1, sides+1)
    #If sides are two, it does a coin toss as the dice roll
    if sides == 2 and randomNumber == 1:
        print("You flip a coin.. and it lands on.. HEADS")
    elif sides == 2 and randomNumber == 2:
        print("You flip a coin.. and it lands on.. TAILS")
    else:
        print("You roll a %d sided die... and it lands on %d!" % (sides, randomNumber))
        #Checks if dice rolls on lowest possible value, does not mean the program is failing
        if randomNumber == 1:
            print("Critical failure!")
        #Checks if dice rolls on the highest possible value
        elif randomNumber == sides:
            print("Critical success!")
    return randomNumber


def roller():
    try:
        sides = int(input("How many sides would you like your die to have?"))
        if sides < 2:
            raise ValueError
    except ValueError:
        print("ERROR Invalid entry: Must be an integer greater than 1.")
        return
    randomNumber = random.randrange(1, sides+1)
    if sides == 2 and randomNumber == 1:
        print("You flip a coin.. and it lands on.. HEADS")
    elif sides == 2 and randomNumber == 2:
        print("You flip a coin.. and it lands on.. TAILS")
    else:
        print("You roll a %d sided die... and it lands on %d!" % (sides, randomNumber))
        if randomNumber == 1:
            print("Critical failure!")
        elif randomNumber == sides:
            print("Critical success!")
    return randomNumber


#Takes user back to start of program if they wish to continue, or ends the program if finished
finished = False
while not finished:
    rollerWith(6)
    answer = input("Continue? Y/N").upper()
    if answer == "N":
        finished = True

