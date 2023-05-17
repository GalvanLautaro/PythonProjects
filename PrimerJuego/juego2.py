import random

def randomNumber():
    return random.randint(0, 99)

def enterNumber():
    selectedNumber = -1
    while selectedNumber < 0 or selectedNumber > 99:
        selectedNumber = int(input("Guess the number between 0 and 99: "))
    return selectedNumber

def hints(n, r):
    if n == r:
        print("You won!")
        print("Random number was: " + str(r))
        return True;
    else:
        if n < r:
            print("Too small")
        else:
            print("Too big")
    return False

def play():
    randN = randomNumber()
    attemptsCont = 0
    flag = False

    while flag != True:
        num = enterNumber()
        flag = hints(num, randN)
        attemptsCont += 1

    print("Attempts needed to guess: " + str(attemptsCont))


play()