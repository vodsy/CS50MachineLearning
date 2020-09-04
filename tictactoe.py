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
    x_total = 0
    o_total = 0

    for row in board:
        x_total += row.count(X)
        o_total += row.count(O)


    if x_total > o_total:
        return O
    elif o_total >= x_total:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                action = (i, j)
                possible_actions.add(action)

    return possible_actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise Exception("Invalid actions!!!")

    whichPlayer = player(board)
    newBoard = copy.deepcopy(board)

    newBoard[action[0]][action[1]] = whichPlayer

    return newBoard

# Use generator
def _lines(board):
    yield from board
    yield [board[i][i] for i in range(len(board))] # One of the diagonals

def lines(board):
    yield from _lines(board)
    # Rotate board 90 degrees to get columns and other diagonal
    yield from _lines(list(zip(*reversed(board))))

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for line in lines(board):
        if len(set(line)) == 1 and line[0] is not None:
            return line[0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    who_won = winner(board)
    free_spaces = actions(board)

    if who_won is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False

    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who_won = winner(board)

    if who_won == X:
        return 1
    elif who_won == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    current_actions = actions(board)

    if current_player == X:
        v = -math.inf
        best_move = set()
        for action in current_actions:
            foo = min_value(result(board, action))
            if foo > v:
                v = foo
                best_move = action
    else:
        v = math.inf
        best_move = set()
        for action in current_actions:
            foo = max_value(result(board, action))
            if foo < v:
                v = foo
                best_move = action
    return best_move

def max_value(board):

    possible_actions = actions(board)

    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in possible_actions:
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    possible_actions = actions(board)

    if terminal(board):
        return utility(board)
    v = math.inf
    for action in possible_actions:
        v = min(v, max_value(result(board, action)))
    return v
