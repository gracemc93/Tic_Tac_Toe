import game_functions as game

# Main
# Setup for first game
game_board = game.start_board()
player_one = game.start_game()
player_two = ''
player_one_wins = 0
player_two_wins = 0
replay = 'y'
turn = 1

while replay == 'y':
    game_board = game.start_board()
    if player_one == 'x':
        player_two = 'o'
    elif player_one == 'o':
        player_two = 'x'

    game.display_board(game_board)
    game_board = game.take_turn(game_board, turn, player_one, player_two)
    winner = game.check_win(game_board)
    game.display_board(game_board)

    while winner != 'x' and winner != 'o' and winner != 'y':
        turn = game.get_turn(turn)
        game_board = game.take_turn(game_board, turn, player_one, player_two)
        winner = game.check_win(game_board)
        game.display_board(game_board)

    if winner == player_one:
        print("\nPlayer One Wins!")
        player_one_wins = player_two_wins+1
    elif winner == player_two:
        print("\nPlayer Two Wins!")
        player_two_wins = player_two_wins+1
    elif winner == 'y':
        print("\nNo Winner!")

    replay = input("\nWould you like to replay? (y/n) ")
    if replay == 'n':
        print("\nThanks for playing, final scores are: \nPlayer One: ", player_one_wins, "\nPlayer Two Scores",
              player_two_wins)
        break
