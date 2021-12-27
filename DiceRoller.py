import random
import logging

#Configuring log
logging.basicConfig(
    filename='mylog.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')

#intial log message that lets us now that the program was executed successfully
logging.info("Program runs, logging information here")


def roller():
    try:
        sides = int(input("How many sides would you like your die to have?"))
        if sides < 2:
            raise ValueError
    except ValueError:
        print("ERROR Invalid entry: Must be an integer greater than 1.")
        #Logs an error message if the user enters a number less than 2
        logging.error("Invalid Entry: Must be an integer greater than 1")
        return
    randomNumber = random.randrange(1, sides+1)
    if sides == 2 and randomNumber == 1:    #If sides are two, it does a coin toss as the dice roll
        #Logs an info message if the user flips a coin and its result
        logging.info("Successful coin flip: HEADS")
        print("You flip a coin.. and it lands on.. HEADS")
    elif sides == 2 and randomNumber == 2:
        #Logs an info message if the user flips a coin and its result
        logging.info("Successful coin flip: TAILS")
        print("You flip a coin.. and it lands on.. TAILS")
    else:
        #Logs an info message if the user rolls a n sided die and its result
        logging.info("Successful roll of a %d sided die and lands on: %d" % (sides,randomNumber))
        print("You roll a %d sided die... and it lands on %d!" % (sides, randomNumber))
        if randomNumber == 1: #Checks if dice rolls on lowest possible value, does not mean the program is failing
            print("Critical failure!")
        elif randomNumber == sides: #Checks if dice rolls on the highest possible value
            print("Critical success!")
    return randomNumber

#Takes user back to start of program if they wish to continue, or ends the program if finished
finished = False
while not finished:
    roller()
    answer = input("Continue? Y/N").upper()
    if answer == "N":
        finished = True

#Logs a message telling you that the program exited successfully
logging.info("Program ends, end of logging")