import sys
import random

availableChoices = ["r", "p", "s"]

def printHeader():
    print("ROCK, PAPER, SCISSORS")
    print(str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")


def showdown(userChoice):
# while True:
    printHeader()
    # userChoice = input().lower()
    computerChoice = availableChoices[random.randint(0, 2)]

    if userChoice == "r":
        print("ROCK versus...")
        if computerChoice == "s":
            print("SCISSORS")
            print("You win!")
            return 1, 0, 0

        if computerChoice == "p":
            print("PAPER")
            print("You lose!")
            return 0, 1, 0

        if computerChoice == "r":
            print("ROCK")
            print("It's a tie!")
            return 0, 0, 1

    elif userChoice == "p":
        print("PAPER versus...")
        if computerChoice == "s":
            print("SCISSORS")
            print("You lose!")
            return 1, 0, 0

        if computerChoice == "r":
            print("ROCK")
            print("You win!")
            return 0, 1, 0

        if computerChoice == "p":
            print("PAPER")
            print("It's a tie!")
            return 0, 0, 1

    elif userChoice == "s":
        if computerChoice == "r":
            print("ROCK")
            print("You lose!")
            return 1, 0, 0

        if computerChoice == "p":
            print("PAPER")
            print("You win!")
            return 0, 1, 0

        if computerChoice == "s":
            print("s")
            print("It's a tie!")
            return 0, 0, 1

    elif userChoice == "q":
        sys.exit()


    print(" ")

    return computerChoice


