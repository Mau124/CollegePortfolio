from simpleai.search import SearchProblem, breadth_first, depth_first

class Problem3(SearchProblem):
    
    capacity = (8, 5, 3)

    def __init__(self):
        SearchProblem.__init__(self, (8, 0, 0))

    def actions(self, state):
        act = []
        # A -> B
        act.append(self.transfer(state, 0, 1))

        # A -> C
        act.append(self.transfer(state, 0, 2))
        
        # B -> A
        act.append(self.transfer(state, 1, 0))

        # B -> C
        act.append(self.transfer(state, 1, 2))

        # C -> A
        act.append(self.transfer(state, 2, 0))

        # C -> B
        act.append(self.transfer(state, 2, 1))

        return act

    def result(self, state, action):
        result_state = list(state)

        result_state[action[0]] -= action[2]
        result_state[action[1]] += action[2]

        return tuple(result_state)

    def is_goal(self, state):
        return state[0] == state[1] and state[2] == 0
    
    def transfer(self, state, index_giver, index_taker):
        left = self.capacity[index_taker] - state[index_taker]

        if state[index_giver] >= left:
            return (index_giver, index_taker, left)
        else:
            return (index_giver, index_taker, state[index_giver])

print("Using Breadth First Search")
result_breadth_first = breadth_first(Problem3(), graph_search=True)
result_breadth_first.path()

for i, (action, state) in enumerate(result_breadth_first.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result_breadth_first.path()) - 1:
        print('After moving', action, 'Goal achieved!')
    else:
        print('After moving', action)

    print(state)

print("Using Depth First Search")
result_depth_first = depth_first(Problem3(), graph_search=True)
result_depth_first.path()

for i, (action, state) in enumerate(result_depth_first.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result_depth_first.path()) - 1:
        print('After moving', action, 'Goal achieved!')
    else:
        print('After moving', action)

    print(state)