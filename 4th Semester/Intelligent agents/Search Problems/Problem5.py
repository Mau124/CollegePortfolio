from simpleai.search import SearchProblem, astar

# -------------------------------------------------------------------------------------------------------------------
#                                               Solving Labyrinth
# -------------------------------------------------------------------------------------------------------------------

class Problem5(SearchProblem):

    HORIZONTAL = [0, 1, 0, -1]
    VERTICAL = [-1, 0, 1, 0]

    def __init__(self, initial_state, target_state, obstacle_matrix):
        self.target_state = target_state
        self.obstacle_matrix = obstacle_matrix

        self.rows = len(obstacle_matrix)
        self.cols = len(obstacle_matrix[0])

        SearchProblem.__init__(self, initial_state)

    def actions(self, state):
        act = []

        for i in range(4):
            idy = state[0] + self.VERTICAL[i]
            idx = state[1] + self.HORIZONTAL[i]

            if (idy >= 0 and idy < self.rows and idx >= 0 and idx < self.cols and self.obstacle_matrix[idy][idx] != '+'):
                act.append((idy, idx))

        return act

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.target_state

    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        x2 = self.target_state[1]
        x1 = state[1]
        
        y2 = self.target_state[0]
        y1 = state[0]

        distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

        return distance


# -------------------------------------------------------------------------------------------------------------------
#                                          Main Program
# -------------------------------------------------------------------------------------------------------------------

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()

obstacle_matrix =  [list('++++++++++++++++++++++'),
                    list('+   +   ++           +'),
                    list('+     +     +++++++ ++'),
                    list('+ +    ++  ++++ +++ ++'),
                    list('+ +   + + ++    +    +'),
                    list('+          ++  ++O + +'),
                    list('+++++ + +      ++  + +'),
                    list('+++++ +++  + +  ++   +'),
                    list('+          + ++++ +  +'),
                    list('+++++X+  + + +       +'),
                    list('++++++++++++++++++++++')]

initial_position = ()
target_position = ()

for i in range(len(obstacle_matrix)):
    for j in range(len(obstacle_matrix[i])):
        if obstacle_matrix[i][j] == 'O':
            initial_position = (i, j)
        
        if obstacle_matrix[i][j] == 'X':
            target_position = (i, j)

result = astar(Problem5(initial_position, target_position, obstacle_matrix), graph_search=True)

print("Mapa antes de encontrar un camino")
print_matrix(obstacle_matrix)

for i, (action, state) in enumerate(result.path()):
    if action != None and i < len(result.path())-1:
        obstacle_matrix[state[0]][state[1]] = '#'

print("Mapa despues de encontrar un camino")
print_matrix(obstacle_matrix)