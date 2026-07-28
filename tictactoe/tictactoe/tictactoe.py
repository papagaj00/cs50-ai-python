"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    parity = sum(row.count(EMPTY) for row in board)%2

    if parity == 1:
        return "X"
    else:
        return "O"

    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves

    raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action

    if i < 0  or i > 2 or j < 0 or j > 2:
        raise ValueError("Invalid : out of bounds")

    if board[i][j] != EMPTY:
         raise ValueError("Invalid : occupied square")

    new_board = copy.deepcopy(board)

    new_board[i][j] = player(board)

    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
            ]

    for win in wins:
         if board[win[0][0]][win[0][1]] == board[win[1][0]][win[1][1]] == board[win[2][0]][win[2][1]]:
            if board[win[0][0]][win[0][1]] == "X":
                return "X"
            elif board[win[0][0]][win[0][1]] == "O":
                 return "O"

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if sum(row.count(EMPTY) for row in board) == 0:
        return True
    elif winner(board) != None:
        return True
    else:
        return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if player(board) == "X":

        best_score = float("-inf")
        best_action = None

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    if player(board) == "O":

        best_score = float("inf")
        best_action = None

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

        return best_action

    raise NotImplementedError
