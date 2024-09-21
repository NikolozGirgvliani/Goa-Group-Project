def print_board(board):
    # Prints the board in a grid format
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    
    # Check if any win condition is met
    for condition in win_conditions:
        if condition.count(player) == 3:
            return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    turns = 0

    while turns < 9:
        print_board(board)
        print(f"Player {current_player}'s turn. Enter row and column (0, 1, or 2):")
        
        try:
            row, col = map(int, input("Row and Column (e.g., '1 2'): ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                turns += 1
                
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    return
                
                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken. Choose another one.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")

    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()