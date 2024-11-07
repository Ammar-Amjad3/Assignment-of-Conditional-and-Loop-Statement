# Write a program that continues to ask for a number until the correct number is guessed.

import random

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)

while True:
    
    # Ask the user to enter a guess
    guess = int(input("Guess the number between 1 and 100: "))

    # Check if the guess is correct
    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < correct_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
