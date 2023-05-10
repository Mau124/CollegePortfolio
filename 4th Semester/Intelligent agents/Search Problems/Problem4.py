#------------------------------------------------------------------------------------------------------------------
#   8-puzzle solver using the A* algorithm
#
#   This code is an adaptation of the 8-puzzle solver described in:
#   Artificial intelligence with Python. Alberto Artasanchez and Prateek Joshi. 2nd edition, 2020, 
#   editorial Pack. Chapter 10.
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from simpleai.search import astar, SearchProblem
import random

#------------------------------------------------------------------------------------------------------------------
#   Auxiliar functions
#------------------------------------------------------------------------------------------------------------------

def find_empty_space(board):
    """
        This function finds the 2D location of the empty space in a board.

        board: The 2D array that represents the game board.        
    """
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 0:
                return i, j
    return -1,-1

def find_number(board, num):
    """
        This function finds the 2D location of the specified number in a board.

        board: The 2D array that represents the game board. 
        num: The number to be found.
    """
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == num:
                return i, j
    return -1,-1


def random_movements(board, n):
    """
        This function returns a new board after performing n random movements on the specified board.

        board: The 2D array that represents the input game board.  
    """
    new_board = [list(r) for r in board]
    e_row, e_col = find_empty_space(new_board)
    board_size = len(new_board)    

    for i in range(n):
        mov_ok = False
        while not mov_ok:
            mov = random.randint(1,4)
            if mov == 1 and e_row > 0:
                new_board[e_row][e_col], new_board[e_row-1][e_col] = \
                    new_board[e_row-1][e_col], new_board[e_row][e_col]
                e_row-=1
                mov_ok = True
            elif mov == 2 and e_row < board_size-1:    
                new_board[e_row][e_col], new_board[e_row+1][e_col] = \
                    new_board[e_row+1][e_col], new_board[e_row][e_col]
                e_row+=1
                mov_ok = True
            elif mov == 3 and e_col > 0:
                new_board[e_row][e_col], new_board[e_row][e_col-1] = \
                    new_board[e_row][e_col-1], new_board[e_row][e_col]
                e_col-=1
                mov_ok = True
            elif mov == 4 and e_col < board_size-1: 
                new_board[e_row][e_col], new_board[e_row][e_col+1] = \
                    new_board[e_row][e_col+1], new_board[e_row][e_col]
                e_col+=1
                mov_ok = True
    return tuple(tuple(row) for row in new_board);

#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

class EightPuzzleProblem(SearchProblem):
    """ Class that is used to define 8-puzzle problem. 
        The states are represented by 2D touples ((a,b,c),(d,e,f),(g,h,i)), where each element is one
        number from 0 to 8. The number 0 indicates the possition of the empty tile.
    """
    
    def __init__(self, initial_state):
        """ 
            This constructor initializes the 8-puzzle problem. 
        
            initial_state: The initial state of the board.
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, initial_state)

        # Define goal state.
        self.goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))        

    def actions(self, state):
        """ 
            This method returns a list with the possible actions that can be performed according to
            the specified state.

            state: The state to be evaluated.
        """
        row_empty, col_empty = find_empty_space(state)

        actions = []
        if row_empty > 0:
            actions.append([row_empty - 1, col_empty])
        if row_empty < 2:
            actions.append([row_empty + 1, col_empty])
        if col_empty > 0:
            actions.append([row_empty, col_empty - 1])
        if col_empty < 2:
            actions.append([row_empty, col_empty + 1])

        return actions
        
    def result(self, state, action):
        """ 
            This method returns the new state obtained after performing the specified action.

            state: The state to be modified.
            action: The action be perform on the specified state.
        """
                
        new_board = [list(r) for r in state]

        row_old, col_old = find_empty_space(state)  # Current empty position
        row_new, col_new = action;                  # New empty position

        # Swap values
        new_board[row_old][col_old], new_board[row_new][col_new] = \
            new_board[row_new][col_new], new_board[row_old][col_old]

        return tuple(tuple(row) for row in new_board)
        
    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        return state == self.goal

    def cost(self, state, action, state2):
        """ 
            This method receives two states and an action, and returns
            the cost of applying the action from the first state to the
            second state.

            state: The initial state.
            action: The action used to generate state2.
            state2: The state obtained after applying the specfied action.
        """
        return 1

    def heuristic(self, state):
        """ 
            This method returns an estimate of the distance from the specified state to 
            the goal.

            state: The state to be evaluated.
        """
        
        distance = 0

        for row_goal, row in enumerate(self.goal):
            for col_goal, item in enumerate(row):

                target_number = self.goal[row_goal][col_goal]
                row_current, col_current = find_number(state, target_number)

                ############## Heuristic function 1 (Hamming distance)
                # Is the element in the right position?
                #distance += int(row_current != row_goal or col_current != col_goal)
                ##############

                ############## Heuristic function 2 (Mahattan distance)
                # Distance between the goal position and the current position
                distance += abs(row_current - row_goal) + abs(col_current - col_goal)
                ##############

        return distance

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Initialize board
initial_board = random_movements(((0, 1, 2), (3, 4, 5), (6, 7, 8)), 1000)

# Solve problem
result = astar(EightPuzzleProblem(initial_board), graph_search=True)

# Print results
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'into the empty space. Goal achieved!')
    else:
        print('After moving', action, 'into the empty space')

    for row in state:
        for item in row:
            print("{:2}".format(item), end = " ")
        print()

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
