import random

name = input("Hello, what's your name? ")
print(name, ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number, please.")

randomInt = random.randint(0,101)

def playGame():
    tries = 0
    guess = 0

    while guess != randomInt:
        guess = int(input("Your guess? "))
        if guess > randomInt:
            print("Your guess is too high, try again.")
            tries += 1
           
        elif guess < randomInt:
            print("Your guess is too low, try again.")
            tries += 1
        else:
            tries += 1
            print("Congratulations ", name, "! You found my number in ", tries, "tries!")

playGame()