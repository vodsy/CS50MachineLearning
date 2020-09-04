from tictactoe import *

X = "X"
O = "O"

# Test winner
boardWinner = [
    [O, O, X],
    [X, X, O],
    [X, X, O]
    ]
#print(winner(boardWinner))


# Test result and player
resultBoard = [
    [O, X, O],
    [X, X, None],
    [X, O, None]
]
action = (2, 2)
#print(result(resultBoard, action))


# Test actions
possibleActionsBoard = [
    [O, X, O],
    [X, X, None],
    [X, O, None]
]
#print(actions(possibleActionsBoard))

# Test terminal
terminalTestBoard = [
    [O, O, X],
    [X, X, O],
    [O, X, None]
    ]
#print(terminal(terminalTestBoard))

utilityBoard = [
    [O, O, X],
    [X, X, O],
    [O, X, O]
    ]
#print(utility(utilityBoard))
