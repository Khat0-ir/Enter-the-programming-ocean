import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            file = open('result.txt','a')
            file.write(f"your game had {attempts} \n")
            file.close

            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")


guessing_game()
