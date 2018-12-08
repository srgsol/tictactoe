"""
Tic Tac Toe AI game

The Tic Tac Toe game(http://en.wikipedia.org/wiki/Tic-tac-toe), is an 
adversarial game(http://www.cs.sfu.ca/CourseCentral/310/oschulte/mychapter5.pdf)
which can be modeled with a game tree(http://en.wikipedia.org/wiki/Game_tree) 
and can be solved with the minimax algorithm(http://www.cs.berkeley.edu/~kamil/teaching/sp03/minimax.pdf). 
It is also worth to see the game complexity(http://en.wikipedia.org/wiki/Game_complexity)


Sergi Soler i Segura
"""
import os
import copy

from tictactoe.minimax import minimax, is_winning, is_tie, switch_player

# Initial game state.
s0 = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def game_loop():
    """Play a game and when finished, asks user to play again."""
    print_welcome_screen()
    play()
    while play_again():
        print_welcome_screen()
        play()


def play_again():
    """Ask user to play again. Gather response."""
    again = input("Do you want to play again [y/n]? ")
    if again.lower() == 'y':
        return True
    elif again.lower() == 'n':
        print('Bye!')
        return False
    else:
        # If invalid input, ask again.
        return play_again()


def play():
    """Main game function."""
    state = copy.deepcopy(s0)

    player = start_game()

    while True:
        if player == 'o':
            pos = input("Your turn: ")
        else:
            print("A.I. turn... ")
            pos = minimax(state)

        try:
            move(state, int(pos), player)
        except:
            # if invalid move, do not check for
            # game over and do not switch player.
            continue

        print_board(state)

        if is_winning(state, player):
            print('Player', player, 'win!')
            break
        if is_tie(state):
            print('Game over. Ties')
            break
        player = switch_player(player)

    return


def start_game():
    """Ask user if he wants to move first."""
    player = input("Who starts the game? You or A.I.? [Y|A]:")
    if player in ['Y', 'y']:
        return 'o'
    elif player in ['A', 'a']:
        return 'x'
    else:
        start_game()


def move(state, pos, player):
    """Check if the given move is valid."""
    # Convert the given position in row, column format
    if pos < 3:
        i = 0
        j = pos
    if 2 < pos < 6:
        i = 1
        j = pos - 3
    if 5 < pos:
        i = 2
        j = pos - 6

    # Check if it is a vaild position,
    if state[i][j] != ' ':
        print('Invalid move')
        raise Exception
    else:
        state[i][j] = player


def print_board(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end='')
            if j < 2:
                print(' | ', end='')
            else:
                print(' ')
        if i < 2:
            print('--+---+--')
    print(2 * '\n')
    return


def print_welcome_screen():
    os.system('clear')
    print("This are the board positions:")
    print_board([['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']])


def main():
    game_loop()


if __name__ == '__main__':
    main()
