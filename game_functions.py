#Functions used for Tic Tac Toe game
def start_game():
    print("WELCOME TO TIC TAC TOE\n")
    player_one = input("\nPlayer one, 'x' or 'o'? ")
    print("\n")
    return player_one


def start_board():
    game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return game_board


def take_turn(game_board, turn, player_one, player_two):
    if turn == 1:
        position = input("\nPlayer one, pick a position: ")
        test_int = int(position)
        # print(game_board[test-1])
        game_board[test_int - 1] = player_one

    if turn == 2:
        position = input("\nPlayer two, pick a position: ")
        test_int = int(position)
        game_board[test_int - 1] = player_two
        print("\nGame Board position", game_board[test_int - 1])

    return game_board


def display_board(game_board):
    print("|", game_board[0], "|", game_board[1], "|", game_board[2], "|\n-------------")
    print("|", game_board[3], "|", game_board[4], "|", game_board[5], "|\n-------------")
    print("|", game_board[6], "|", game_board[7], "|", game_board[8], "|\n-------------")


def check_win(game_board):
    if game_board[0] == 'x' and game_board[1] == 'x' and game_board[2] == 'x':
        winner = 'x'
        return winner;
    elif game_board[0] == 'o' and game_board[1] == 'o' and game_board[2] == 'o':
        winner = 'o'
        return winner
    elif game_board[3] == 'x' and game_board[4] == 'x' and game_board[5] == 'x':
        winner = 'x'
        return winner;
    elif game_board[3] == 'o' and game_board[4] == 'o' and game_board[5] == 'o':
        winner = 'o'
        return winner;
    elif game_board[6] == 'x' and game_board[7] == 'x' and game_board[8] == 'x':
        winner = 'x'
        return winner;
    elif game_board[6] == 'o' and game_board[7] == 'o' and game_board[8] == 'o':
        winner = 'o'
        return winner;
    elif game_board[0] == 'x' and game_board[3] == 'x' and game_board[6] == 'x':
        winner = 'x'
        return winner;
    elif game_board[1] == 'x' and game_board[4] == 'x' and game_board[7] == 'x':
        winner = 'x'
        return winner
    elif game_board[2] == 'x' and game_board[5] == 'x' and game_board[8] == 'x':
        winner = 'x'
        return winner
    elif game_board[0] == 'x' and game_board[4] == 'x' and game_board[8] == 'x':
        winner = 'x'
        return winner
    elif game_board[2] == 'x' and game_board[4] == 'x' and game_board[6] == 'x':
        winner = 'x'
        return winner
    elif game_board[0] == 'o' and game_board[3] == 'o' and game_board[6] == 'o':
        winner = 'o'
        return winner
    elif game_board[1] == 'o' and game_board[4] == 'o' and game_board[7] == 'o':
        winner = 'o'
        return winner
    elif game_board[2] == 'o' and game_board[5] == 'o' and game_board[8] == 'o':
        winner = 'o'
        return winner
    elif game_board[0] == 'o' and game_board[4] == 'o' and game_board[8] == 'o':
        winner = 'o'
        return winner
    elif game_board[2] == 'o' and game_board[4] == 'o' and game_board[6] == 'o':
        winner = 'o'
        return winner
    else:
        for x in range(1, 9):
            if game_board[x] != 'x' or 'o':
                check_full = 'n'
                return check_full
            else:
                check_full = 'y'
                return check_full


def get_turn(turn):
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    print(turn)
    return turn
