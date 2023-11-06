import random
import numpy as np


def create_board():
    return np.array([' '] * 10)


def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])



def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O? ').upper()
    return ['X', 'O', 'player'] if letter == 'X' else ['O', 'X', 'computer']


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not board[int(move)] == ' ':
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def get_empty_cells(board):
    return np.where(board == ' ')[0]


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    return any(all(board[c] == letter for c in combo) for combo in winning_combinations)


def is_board_full(board):
    return ' ' not in board[1:]


def choose_random_move(board):
    preferred = [[1, 3, 7, 9], [5], [2, 4, 6, 8]]
    available = get_empty_cells(board)
    for i in preferred:
        places = np.intersect1d(i, available)
        if places.size:
            return np.random.choice(places)


def computer_move(board, computer):
    player = 'X' if computer == 'O' else 'O'
    opponent_wining_pos = None
    for pos in get_empty_cells(board):
        copy = board.copy()
        make_move(copy, computer, pos)
        if is_winner(copy, computer):
            return pos
        make_move(copy, player, pos)
        if is_winner(copy, player):
            opponent_wining_pos = pos

    if opponent_wining_pos:
        return opponent_wining_pos

    return choose_random_move(board)


print('Welcome to Tic Tac Toe!')

board = create_board()

player, computer, turn = input_player_letter()

while True:
    if turn == 'player':
        print_board(board)
        move = get_player_move(board)
        make_move(board, player, move)

        if is_winner(board, player):
            print_board(board)
            print('Hooray! You have won the game!')
            break
        elif is_board_full(board):
            print_board(board)
            print('The game is a tie!')
            break
        else:
            turn = 'computer'

    else:
        move = computer_move(board, computer)
        make_move(board, computer, move)

        if is_winner(board, computer):
            print_board(board)
            print('The computer has beaten you! You lose.')
            break
        elif is_board_full(board):
            print_board(board)
            print('The game is a tie!')
            break
        else:
            turn = 'player'
