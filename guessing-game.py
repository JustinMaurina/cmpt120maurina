# This is a guessing game.

answer = 'Kangaroo'

while 1==1:
    print("The program is thinking of an animal.")
    print("Guess the animal.")
    if input() == answer:
        print("That was the animal. Good job!")
        break
    else:
        print("That was not the animal. Please try again!")
