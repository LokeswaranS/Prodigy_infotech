import random

def play_guessing_game():
    print("Welcome to the Guessing Game!")
    print("----------------------------")

    lower_bound = 1  # Lower bound of the number range
    upper_bound = 100  # Upper bound of the number range
    secret_number = random.randint(lower_bound, upper_bound)  # Generate a random number

    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try guessing higher.")
            elif user_guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {secret_number} correctly.")
                print(f"It took you {attempts} attempts to win!")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    play_guessing_game()
