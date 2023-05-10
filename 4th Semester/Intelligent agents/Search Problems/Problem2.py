from simpleai.search import SearchProblem, breadth_first, depth_first

class Problem2(SearchProblem):
    N_POINTS = 6

    def __init__(self):
        SearchProblem.__init__(self, (0, 0, 0, 0, 0, 0))

    def actions(self, state):
        position = self.N_POINTS - state.count(0)

        act = []
        for candidate in range(1, 7):
            if candidate not in state:
                act.append((position, candidate))

        return act

    def result(self, state, action):
        result_state = list(state)
        result_state[action[0]] = action[1]
        return tuple(result_state)

    def is_goal(self, state):
        return ((state[0] + state[1] + state[2] == 10) and
                (state[2] + state[3] + state[4] == 10) and
                (state[4] + state[5] + state[0] == 10) and
                state.count(0) == 0)

result_breadth_first = breadth_first(Problem2(), graph_search=False)
result_depth_first = depth_first(Problem2(), graph_search=False)