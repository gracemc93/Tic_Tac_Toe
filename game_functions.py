# Functions used for Tic Tac Toe game
def start_game():
    player_one = input("\nPlayer one, 'x' or 'o'? ")
    print("\n")

    if check_valid_symbol(player_one) == True:
        return player_one
    else:
        start_game()

# Set board to starting state
def start_board():
    game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return game_board

# Function to handle a move
def take_turn(game_board, turn, player_one, player_two):
    if turn == 1:
        position = input("\nPlayer one, pick a position: ")
        while check_valid_position(position) != True:
            position = input("Position invalid, please enter another: ")
        while position_status(game_board, position) != True:
            position = input("This position is taken, chose another")

        position_int = int(position)
        game_board[position_int - 1] = player_one

    if turn == 2:
        position = input("\nPlayer two, pick a position: ")
        while check_valid_position(position) != True:
            position = input("Position invalid, please enter another: ")
        while position_status(game_board, position) != True:
            position = input("This postion is taken, chose another")

        position_int = int(position)
        game_board[position_int - 1] = player_two

    return game_board


# Print 3x3 board
def display_board(game_board):
    for x in range(0, 8, 3):
        print("|", game_board[x], "|", game_board[x + 1], "|", game_board[x + 2], "|\n-------------")


# Checks the board for a winning combo
def check_win(game_board):
    # Check across for winner
    for x in range(0, 8, 3):
        if game_board[x] == 'x' and game_board[x + 1] == 'x' and game_board[x + 2] == 'x':
            winner = 'x'
            return winner
        elif game_board[x] == 'o' and game_board[x + 1] == 'o' and game_board[x + 2] == 'o':
            winner = 'o'
            return winner

    # Check down for winner
    for x in range(3):
        if game_board[x] == 'x' and game_board[x + 3] == 'x' and game_board[x + 6] == 'x':
            winner = 'x'
            return winner
        elif game_board[x] == 'o' and game_board[x + 3] == 'o' and game_board[x + 6] == 'o':
            winner = 'o'
            return winner

    # Check diagonally for winner
    for x in range(1):
        if game_board[x] == 'x' and game_board[x + 4] == 'x' and game_board[x + 8] == 'x':
            winner = 'x'
            return winner
        elif game_board[x] == 'o' and game_board[x + 4] == 'o' and game_board[x + 8] == 'o':
            winner = 'o'
            return winner
        elif game_board[x + 2] == 'x' and game_board[x + 4] == 'x' and game_board[x + 6] == 'x':
            winner = 'x'
            return winner
        elif game_board[x + 2] == 'o' and game_board[x + 4] == 'o' and game_board[x + 6] == 'o':
            winner = 'o'
            return winner

    # Check if board is full
    counter = 0
    for x in range(1, 9):
        if game_board[x] != 'x' or game_board[x] != 'o':
            counter = counter + 1
    if counter > 0:
        check_full = 'n'
        return check_full
    elif counter == 0:
        check_full = 'y'
        return check_full

# Switches user turns
def get_turn(turn):
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn

# Checks if a position has already been occupied
def position_status(game_board, position):
    position_int = int(position)
    if game_board[position_int - 1] != 'x' and game_board[position_int - 1] != 'o':
        return True
    else:
        return False

# Check that symbol is only 'x' or 'o'
def check_valid_symbol(player_one):
    if player_one == 'x' or player_one == 'o':
        return True
    else:
        print("Invalid symbol, must be 'x' or 'o'")
        return False

# Check position input is valid
def check_valid_position(position):
    valid_position = False
    starting_gameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in range(8):
        if starting_gameboard[x] == position:
            valid_position = True
    return valid_position
