# Game #2

food = 'banana' #Word
attempts = 0

print('Welcome to GUESS THE FOOD game!')  #Welcome
print('Try To Guess The food!')   #Guess

print('HINT: Monkeys Like This Food')  #Hint
user_input = input('Guess: ')

user_input = user_input
attempts += 1

while True:
    user_input = input('Guess: ')   #ვიყენებთ while true რათა გავაკეთოთ infinite loop
    attempts += 1

    if user_input == food:
        print(f'Congratulations! You guessed the food: {food.capitalize()} in {attempts} attempts.')  #შენ გამოიცანი
        break
    else:
        print('You guessed wrong! Try again.')   #ვერ გამოიცანი
