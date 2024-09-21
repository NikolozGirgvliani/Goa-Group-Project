import random

def game4():
    choices = ['rock', 'paper', 'scissors']
    ai_coise = random.choise(choices)

    print('Welcome To Rock-Paper-Scissors')
    print('Choices: Rock, Paper, Scissors')

    user_input = input('Enter Your Choise: ').lower()

    if user_input not in choices:
        print('Invalid Choise. Please choose: Rock, Paper or Scissors')
        return
    
    print(f'AI chose: {ai_coise}')

    if user_input == ai_coise:
        print("it's a tie!")
    elif (user_input == 'rock' and ai_coise == 'scissors') or \
         (user_input == 'paper' and ai_coise == 'rock') or \
         (user_input == 'scissors' and ai_coise == 'paper'):
        print("You win!")
    else:
        print("You lose!")