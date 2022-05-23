"""
Tic Tac Toe Player

video starts @ 1:11:46

"""

import math

from test import min_value

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

    # count the number of moves made by O and X
    xCount = 0
    oCount = 0
    for i in board:
        for j in i:
            if j == X:
                xCount += 1
            elif j == O:
                oCount += 1

    # Determine next player based on player count
    if xCount == oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # initialize empty set of possible moves
    moves = set()

    # check for available moves
    for i, row in enumerate(board):
        for j, space in enumerate(row):
            if space == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # determine move
    row = action[0]
    col = action[1]

    newBoard = initial_state()

    # make next move if possible given the action
    for i, newRow in enumerate(newBoard):
        for j, newSpace in enumerate(newRow):
            if i == row and j == col:
                newBoard[i][j] = player(board)
            else:
                newBoard[i][j] = board[i][j]
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # isolate columns
    col1 = [board[0][0],board[1][0],board[2][0]]
    col2 = [board[0][1],board[1][1],board[2][1]]
    col3 = [board[0][2],board[1][2],board[2][2]]
    
    # isolate rows
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]

    # isolate diagnols
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[2][0], board[1][1], board[0][2]]

    # put all possible checks in a list
    checks = [col1, col2, col3, row1, row2, row3, diag1, diag2]

    # check for winner
    for check in checks:
        # isolate spaces on board
        space1 = check[0]
        space2 = check[1]
        space3 = check[2]

        # update winner, end loop if found
        winner = (space1 == space2 == space3) and (space1 != EMPTY and space2 != EMPTY and space3 != EMPTY)
        if winner:
            return space1 
    
    # if no winner is found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # determine if draw
    checks = []
    for row in board:
        for space in row:
            checks.append(space)

    draw = not any (EMPTY == space for space in checks)
    
    # determine if winner
    won = winner(board) in [X, O]
    
    # if winner or draw terminate
    terminate = draw or won

    return terminate


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # set value based on winner results
    value = {
        None: 0,
        X: 1,
        O: -1
    }

    # determine winner, if there is one
    won = winner(board)
    return value[won]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # corner is optimal first move given the initial state
    if board == initial_state():
        return (0, 0)

    # apply minimax, base starting point on the current player
    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move


def max_value(board):
    """
    minimax helper function
    """

    # determine if game is over
    if terminal(board):
        return utility(board), None

    # determine maximum score after recursing through all the options
    v1 = -math.inf
    m1 = None
    for action in actions(board):
        v2, m2 = min_value(result(board, action))
        if v2 > v1:
            v1 = v2
            m1 = action
    return v1, m1


def min_value(board):
    """
    minimax helper function
    """

    # determine if game is over
    if terminal(board):
        return utility(board), None

    # determine minimum score after recursing through all the options
    v1 = math.inf
    m1 = None
    for action in actions(board):
        v2, act = max_value(result(board, action))
        if v2 < v1:
            v1 = v2
            m1 = action
    return v1, m1
