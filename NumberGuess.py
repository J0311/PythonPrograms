"""

Author: Joseph Walker

This program plays a guessing game with the User. The program
displays a greeting and creates a number between 1 and 100.

The User attempts a guess at the number until a guess equals
the number. If User's guess is too larger or too small, they
will be prompted with a hint.

Once User guess the number, the program displays the total
number of attempts.
"""

import random


class NumberGuess:

    def __init__(self):
        
        ## define the range
        
        self.LOWER = 1
        self.HIGHER = 100

    ## method to generate the random number
        
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    ## game start method
    
    def start(self):
        
        ## generating the random number
        
        random_number = self.get_random_number()

        print(
            f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")

        ## main components of the program
        
        chances = 0
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    f"-> Hurray! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> Your number is less than the random number")
            else:
                print("-> Your number is greater than the random number")
            chances += 1

## instantiating and starting the game
            
numberGuess = NumberGuess()
numberGuess.start()
