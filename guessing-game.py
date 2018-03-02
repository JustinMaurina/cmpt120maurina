# This is a guessing game.

answer1 = 'kangaroo'
answer2 = 'Kangaroo'
answer3 = 'KANGAROO'

while 1==1:
    print("The program is thinking of an animal.")
    print("Guess the animal.")
    if input() == answer1 or answer2 or answer3:
        print("That was the animal. Good job!")
        break
    else:
        print("That was not the animal. Please try again!")
    if input() == 'quit':
        print("Thanks for plaiying.")
        break
        
