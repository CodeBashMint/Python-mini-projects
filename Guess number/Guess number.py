import random

def guessing_game():
    num_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess > num_to_guess:
                print("Too high!")
            elif guess < num_to_guess:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        guessing_game()
    else:
        print("Thanks for playing! Goodbye.")

guessing_game()
