import random
import time

def start_game(highscore):
    if highscore > 0:
        print (f"The Previous High Score is {highscore}")
    print("Hello and welcome to the Andrei's Guessing Game")
    time.sleep(2)
    print("You have been chosen due to your exceptional ability to guess numbers")
    time.sleep(2)

    rand = random.randint(1, 101)
    count = 0

    while True:
        try:
            number = int(input("Please guess a number between 1 and 100:   "))
            if number <1 or number > 100:
                print("Hey! I said between 1 and 100! Where are you getting these numbers from...")
                continue
            count += 1
            if number > rand:
                print("Its lower")
            elif number < rand:
                print("Its higher")
            else:
                print("Got it")
                print(f"It took you {count} attempts to guess the number correctly")
                if highscore == 0 or count < highscore:
                    highscore = count
                return highscore

        except ValueError:
            print("That is not a whole number between 1 and 100")



highscore = 0
highscore = start_game(highscore)

while True:
    restart = input("Would you like to try again? (y/n):     ").lower()
    if restart == "y":
        print()
        highscore = start_game(highscore)
    elif restart == "n":
        print("Thank you for playing, see you again!")
        break
    else:
        print("Please answer 'y' or 'n'")