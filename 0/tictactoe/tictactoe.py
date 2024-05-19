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
    
    x=0
    o=0
    
    for row in board:
        for position in row:
            if position == "X":
                x += 1
            elif position == "O":
                o += 1
                
    if x>o:
        return "O"
    else:
        return "X"
    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_actions = set()
    
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == EMPTY:
                possible_actions.add((row, column))
                
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #print(action)
    
    possible_actions = list(actions(board))
    
    #print("Possible Actions:", possible_actions)
    #print("Provided Action:", action)
     
    if action not in possible_actions:
        raise Exception("Not valid action")
    
    new_board = copy.deepcopy(board)
    move = player(new_board)
    new_board[action[0]][action[1]] = move
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    global X
    global O
    
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] =="X") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][0] == "X" and board[1][1] == "X" and board [2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        return X
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] =="O") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (board[0][0] == "O" and board[1][1] == "O" and board [2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) is not None) or all(all(cell is not EMPTY for cell in row) for row in board):
        return True
    else:
        return False


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == "X":
        plays = []
        
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
            
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    elif player(board) == "O":
        plays = []
        
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
            
        return sorted(plays, key=lambda x: x[0])[0][1]
    
def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        #print(action)
        v = max(v, min_value(result(board, action)))
    return v
        
def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        #print(action)
        v = min(v, max_value(result(board, action)))
    return v
