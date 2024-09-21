import random

def coin_toss_game():
    coin = random.choice(['heads', 'tails'])
    print("Welcome to the Coin Toss Game!")
    guess = input("Guess heads or tails: ").lower()

    if guess not in ['heads', 'tails']:
        print("Invalid choice!")
        return

    print(f"The coin landed on {coin}!")

    if guess == coin:
        print("Congratulations! You guessed correctly!")
    else:
        print("Sorry, you guessed wrong.")

coin_toss_game()