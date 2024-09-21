import random
import turtle
import time

# Game 1: Guess the Food
def game1():
    food = 'banana'
    attempts = 0

    print('Welcome to GUESS THE FOOD game!')
    print('Try to guess the food!')
    print('HINT: Monkeys like this food.')

    while True:
        user_input = input('Guess: ')
        attempts += 1

        if user_input.lower() == food:
            print(f'Congratulations! You guessed the food: {food.capitalize()} in {attempts} attempts.')
            break
        else:
            print('You guessed wrong! Try again.')

    return play_again()

# Game 2: Number Guessing Game
def game2():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in less than 5 attempts!")

    while attempts < 5:
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
    else:
        print(f"Sorry, the number was {number_to_guess}.")
    
    return play_again()

# Game 3: Word Guessing Game
def game3():
    word = "giraffe"
    guessed_letters = set()

    print("Welcome to the Word Guessing Game!")
    print("Hint: It's a land animal.")

    while True:
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        guessed_letters.add(guess)

        display = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
        print(display)

        if '_' not in display:
            print("Congratulations! You guessed the word correctly!")
            break

    return play_again()

# Game 4: Rock-Paper-Scissors
def game4():
    choices = ['rock', 'paper', 'scissors']
    while True:
        ai_choice = random.choice(choices)

        print('Welcome to Rock-Paper-Scissors!')
        print('Choices: Rock, Paper, Scissors')

        user_input = input('Enter Your Choice: ').lower()

        if user_input not in choices:
            print('Invalid Choice. Please choose: Rock, Paper, or Scissors')
            continue

        print(f'AI chose: {ai_choice}')

        if user_input == ai_choice:
            print("It's a tie!")
        elif (user_input == 'rock' and ai_choice == 'scissors') or \
             (user_input == 'paper' and ai_choice == 'rock') or \
             (user_input == 'scissors' and ai_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

        if not play_again():
            break

# Game 5: Snake Game
def game5():
    delay = 0.1
    score = 0
    high_score = 0

    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            head.sety(head.ycor() + 20)
        if head.direction == "down":
            head.sety(head.ycor() - 20)
        if head.direction == "left":
            head.setx(head.xcor() - 20)
        if head.direction == "right":
            head.setx(head.xcor() + 20)

    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    while True:
        wn.update()

        # Check for collision with the wall
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        # Check for collision with food
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            score += 10
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        # Move the segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for collision with itself
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                segments.clear()
                score = 0
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)

    wn.bye()

# Game 6: Tic-Tac-Toe
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def game6():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for turn in range(9):
        while True:
            try:
                row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
                col = int(input(f"Player {current_player}, enter col (1-3): ")) - 1
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already taken! Choose another.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a valid row and column (1-3).")

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print("It's a tie!")
    return play_again()

# Game 7: Quiz
def game7():
    questions = [
        {"question": "What is the capital of Georgia?", "answer": "Tbilisi"},
        {"question": "Who wrote 'Vefxistyaosani'?", "answer": "Shota Rustaveli"},
        {"question": "Who won UCL in 2015?", "answer": "Barcelona"},
        {"question": "When did the battle of Didgori happen?", "answer": "1121"},
        {"question": "Who is the GOAT of football?", "answer": "Messi"}
    ]

    score = 0
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").strip()
        if answer.lower() == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"You scored {score} out of {len(questions)}.")
    return play_again()

# Game 8: Coin Toss Game
def game8():
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
    
    return play_again()

# Game 9: Adventure Game
def game9():
    print("Welcome to the Adventure Game!")
    print("You wake up in a forest.")
    print("Your goal is to find a place to stay.")

    first_choice()

def first_choice():
    print("You see two paths before you: Left and Right.")
    choice = input("Which way do you go? (left/right): ").strip().lower()
    if choice == "left":
        haunted_house()
    elif choice == "right":
        treasure_room()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_choice()

def haunted_house():
    print("\nYou saw a haunted house.")
    print("Something is chasing you. Think fast!")
    print("Will you enter the house or run?")
    choice = input("Choose an action (run/enter): ").strip().lower()
    if choice == "run":
        print("\nYou got lucky and ran away! Congrats!")
    elif choice == "enter":
        print("\nYou entered the haunted house and ghosts killed you! You lose!")
    else:
        print("Invalid choice. Please type 'run' or 'enter'.")
        haunted_house()

def treasure_room():
    print("\nYou enter a room filled with gold and jewels!")
    print("Congratulations, you found the treasure!")
    print("Do you take some treasure or leave it behind?")
    choice = input("Choose an action (take/leave): ").strip().lower()
    if choice == "take":
        print("\nYou take some treasure and leave the cave. You're rich!")
    elif choice == "leave":
        print("\nYou decide to leave the treasure behind and exit the cave peacefully. A wise choice!")
    else:
        print("Invalid choice. Please type 'take' or 'leave'.")
        treasure_room()

# Play Again Function
def play_again():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    return choice == 'yes'

# Main Menu
def show_home_screen():
    print("Welcome to the PYGAMES!")
    print("1. Play Game 1 - Guess the Food")
    print("2. Play Game 2 - Number Guessing")
    print("3. Play Game 3 - Word Guessing")
    print("4. Play Game 4 - Rock-Paper-Scissors")
    print("5. Play Game 5 - Snake Game")
    print("6. Play Game 6 - Tic-Tac-Toe")
    print("7. Play Game 7 - Quiz")
    print("8. Play Game 8 - Coin Toss")
    print("9. Play Game 9 - Adventure")
    print("0. Exit")

def main():
    while True:
        show_home_screen()
        choice = input("Choose a game (1-9 or 0 to exit): ")

        if choice == '1':
            game1()
        elif choice == '2':
            game2()
        elif choice == '3':
            game3()
        elif choice == '4':
            game4()
        elif choice == '5':
            game5()
        elif choice == '6':
            game6()
        elif choice == '7':
            game7()
        elif choice == '8':
            game8()
        elif choice == '9':
            game9()
        elif choice == '0':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

