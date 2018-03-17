# ttt.py
# subproblems
# Siyu Jia


## 1. create a game board
# parameter: do not need input
# a global variable: a 9-element (like 1-9 or A-I or 9 empty spaces) list
# return: a board with 9 positions (3*3) represented by the elements of the list
def show_board():
    pass


## 2. get players' names or assign roles
# ask the player to choose which role she wants to be by typing 'x' or 'o'


## 3. ask for player's 1st input
# parameter: specify the board
# ask the player to make a move
# return: the player's move
def get_player_move(board):
    pass


## 4. check for invalid moves
# parameters: a board and a move
# return: if a move is valid, return the move; if invalid, ask the player to input again
def check_move(board,move):
    pass


## 5. update the board
# parameter: board,move
# return: replace a postion on the board with a valid move
def update_board(board,move):
    pass


## 6. ask for the second player's input
# parameter: board, the second player/computer's letter
# return: a move
# check for invalid moves
# update the board
def get_computer_move(board,player):
    pass


## 7. check for winner
# parameters: a board and a player's letter
# check if one of the 8 ways to win has been achieved (first, three moves are all made by the same player; second, the combination of the three moves is in the 8 ways to win)
# return: a Boolean, True if the player has won
def check_winner(board,player):
    pass
# or, parameters: a player's letter and her three moves
# check if one of the 8 ways to win has been achieved (first, check if three moves are all made by the player; then, check if the combination of the three moves is in the 8 ways to win)
# return: a Boolean True
def check_player(player,move1,move2,move3):
    pass
def check_winner(player):
    pass


## 8. check a tie (the board is full)
# parameters: board
# return: a Boolean
def check_tie(board):
    pass


## 9. if someone wins, start again or quit the game
# ask the player to choose if she would like to play again
# if the player types 'y', return should be another round of game (re-initialize the board); if she types 'n', end the game
def play_again():
    pass
