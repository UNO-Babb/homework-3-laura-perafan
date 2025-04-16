#Example Flask App for a hexaganal tile game
#Logic is in this python file

# Tic Tac Toe - Simple Python Version

# Initialize empty board
board = [[" " for _ in range(3)] for _ in range(3)]

# Current player symbol: "X" or "O"
current_player = "X"

def display_board():
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(i, " | ".join(row))
        if i < 2:
            print("  ---------")
    print()

def player_move():
    global current_player
    while True:
        try:
            row = int(input(f"{current_player}'s turn. Enter row (0-2): "))
            col = int(input(f"{current_player}'s turn. Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = current_player
                break
            else:
                print("That space is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_draw():
    for row in board:
        if " " in row:
            return False
    return True

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

def play_game():
    display_board()
    while True:
        player_move()
        display_board()
        if check_winner():
            print(f"🎉 {current_player} wins the game!")
            break
        if check_draw():
            print("It's a draw!")
            break
        switch_player()

# Main loop
while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
    reset_game()



