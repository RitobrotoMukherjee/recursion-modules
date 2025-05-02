from math import *

def findSquareRoot(n):
    return sqrt(n)

def findNaturalLogarithm(n):
    return log(n)

def findSineOfNumber(n):
    return sin(n)


def calculator():
    try:
        num = float(input("Enter a number: "))

        print("\nSquare root: %f" %(findSquareRoot(num)))
        print("\nLogarithm: %f" %(findNaturalLogarithm(num)))
        print("\nSine: %f" %(findSineOfNumber(num)))

    except Exception as e:
        print("\nERROR: There are some erros please run the program again")

def startProgram(first = True):
    if first:
        print("\tDo you want to run program? \n")
    try:
        carryOn = True

        while(carryOn):
            choice = input("Y to continue, N to exit: ")

            if(choice == "N" or choice == "n"):
                print("\nTa ta")
                return
            
            calculator()
            carryOn = False
        
    except Exception as e:
        print("\nError occured")
        startProgram(False)

startProgram()