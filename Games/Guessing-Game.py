#Game #1
import random 

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Game Number 1 Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in less than 5 attempts!")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too Low! Try again.")
        elif guess > number_to_guess:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    guessing_game()
