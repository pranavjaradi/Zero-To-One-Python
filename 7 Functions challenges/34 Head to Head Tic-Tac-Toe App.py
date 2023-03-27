"""
Head to Head Tic-Tac-Toe App:
You are responsible for writing a program that will allow two users to play a game of tic tac toe.
Your program should follow the standard rules in which two players alternate turns putting their
pieces, X or O, on a board. If a player has three pieces in a row, either vertically, horizontally,
or diagonally, they are declared the winner. You will represent the tic tac toe board using the
integers 1 through 9 for the 9 spaces on the board. An empty spot on the board will be
represented by an underscore “_”. For example, if a player would like to put a piece in the
center of the board they would enter 5 as their move.
"""

#Definig Function for code

def draw_board(coords):
    """It will print current state of board

    Args:
        coords (list): It will hold the 9 board place information
    """
    print("\n\tTic-Tac-Toe")
    print("\t~~~~~~~~~~~")
    print("\t||{}||{}||{}||".format(coords[0], coords[1], coords[2]))
    print("\t~~~~~~~~~~~")
    print("\t||{}||{}||{}||".format(coords[3], coords[4], coords[5]))
    print("\t~~~~~~~~~~~")
    print("\t||{}||{}||{}||".format(coords[6], coords[7], coords[8]))
    print("\t~~~~~~~~~~~")

def get_player_input(sign, current_board):
    """Function will take the sign of player and the state of current board

    Args:
        sign (string): 'X' or 'O'
        current_board (list): contain the current state of board

    Returns:
        integer : It is place of sign where user want to place it on board ranging from 1 to 9
    """
    while True:
        place = int(input("{}: Where would you like to place your piece (1 - 9): ".format(sign)))
        if place in range(1,10):
            if current_board[place-1] == '_':
                return place
            else:
                print("That spot has already been chosen. Try again.")
        else:
            print("That is not a spot on the board. Try again.")

def place_char_on_board(sign, place, current_board):
    """It will update the board according to player move

    Args:
        sign (string): 'X' or 'O'
        place (integer): It is place of sign where user want to place it on the board ranging from 1 to 9
        current_board (list): contain the current state of board
    """
    current_board[place-1] = sign

def is_winner(sign, current_board):
    """Boolean value for determining winner

    Args:
        sign (string): 'X' or 'O'
        current_board (list): contain the current state of board

    Returns:
        bool: true or false based on sign and current state of board
    """
    return ((current_board[0] == sign and current_board[1] == sign and current_board[2] == sign) or #For top row
            (current_board[3] == sign and current_board[4] == sign and current_board[5] == sign) or #For middle row
            (current_board[6] == sign and current_board[7] == sign and current_board[8] == sign) or #For bottom rom
            (current_board[0] == sign and current_board[3] == sign and current_board[6] == sign) or #For left column
            (current_board[1] == sign and current_board[4] == sign and current_board[7] == sign) or #For middle column
            (current_board[2] == sign and current_board[5] == sign and current_board[8] == sign) or #For right column
            (current_board[0] == sign and current_board[4] == sign and current_board[8] == sign) or #For diagonal left to right
            (current_board[2] == sign and current_board[4] == sign and current_board[6] == sign)) #For diagonal right to left

#Main Code
#Defining user pieces (X or O)
player_1 = 'X'
player_2 = 'O'

#Board state list and numbered board list
current_board = ['_']*9
number_board = [i for i in range(1,10)]

draw_board(number_board) #Drawing board with number to begin game
draw_board(current_board) #Drawing board with current board state

while True:
    place = get_player_input(player_1, current_board)
    place_char_on_board(player_1, place, current_board)
    draw_board(number_board) #Drawing board with number
    draw_board(current_board) #Drawing board with current board state after player 1 move
    if is_winner(player_1, current_board):
        print("Congratulations! Player 1 wins!")
        break
    elif '_' not in current_board:
        print("The game was a Tie!")
        break
    place = get_player_input(player_2, current_board)
    place_char_on_board(player_2, place, current_board)
    draw_board(number_board) #Drawing board with number
    draw_board(current_board) #Drawing board with current board state after player 2 move
    if is_winner(player_2, current_board):
        print("Congratulations! Player 2 wins!")
        break
