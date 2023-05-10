#------------------------------------------------------------------------------------------------------------------
#   Missionaries and cannibals problem
#------------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first

#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

class MissionariesAndCannibals(SearchProblem):
    """ Class that is used to define the missionaries and cannibals problem. 
        The states are represented by tuples (a, b, c, d, e), where a is the number of missionaries 
        on the left side, b is the number of cannibals on the left side, c is the number of 
        missionaries on the right side, d is the number of cannibals on the right side, 
        and e is the position of the raft (L or R).
    """

    def __init__(self):
        """ Class constructor. It initializes the problem with 3 missionaries and 3 cannibals
            at one side of the river. 
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, (3,0,3,0,'L'))

    def actions(self, state):
        """ 
            This method returns a list with the possible actions that can be performed according to
            the specified state.

            state: The state to be evaluated.
        """
        act = []

        if state[4] == 'L':            
            # One missionary to the other side       
            if state[0] >= 1:
                if ((state[0]-1 >= state[2]) or state[0]-1 == 0) and (state[1]+1 >= state[3]):
                    act.append('M1R')

            # Two missionaries to the other side       
            if state[0] >= 2:
                if ((state[0]-2 >= state[2]) or state[0]-2 == 0) and (state[1]+2 >= state[3]):
                    act.append('M2R')

            # One cannibal to the other side       
            if state[2] >= 1:
                if (state[1] >= state[3]+1) or (state[1] == 0):
                    act.append('C1R')

            # Two cannibals to the other side       
            if state[2] >= 2:
                if (state[1] >= state[3]+2) or (state[1] == 0):
                    act.append('C2R')

            # One missionary and one cannibal to the other side       
            if state[0] >= 1 and state[2] >= 1:      
                if state[1]+1 >= state[3]+1:
                    act.append('M1C1R')

        else:
            # One missionary to the other side       
            if state[1] >= 1:
                if ((state[1]-1 >= state[3]) or state[1]-1 == 0) and (state[0]+1 >= state[2]):
                    act.append('M1L')

            # Two missionaries to the other side       
            if state[1] >= 2:
                if ((state[1]-2 >= state[3]) or state[1]-2 == 0) and (state[0]+2 >= state[2]):
                    act.append('M2L')

            # One cannibal to the other side       
            if state[3] >= 1:
                if (state[0] >= state[2]+1) or (state[0] == 0):
                    act.append('C1L')

            # Two cannibals to the other side       
            if state[3] >= 2:
                if (state[0] >= state[2]+2) or (state[0] == 0):
                    act.append('C2L')

            # One missionary and one cannibal to the other side       
            if state[1] >= 1 and state[3] >= 1:    
                if state[0]+1 >= state[2]+1:
                    act.append('M1C1L')

        return act

    def result(self, state, action):
        """ 
            This method returns the new state obtained after performing the specified action.

            state: The state to be modified.
            action: The action be perform on the specified state.
        """

        m1 = state[0]
        m2 = state[1]    
        c1 = state[2]            
        c2 = state[3]
        r = state[4]

        if action == 'M1R':
            m1-=1;
            m2+=1;
            r='R';
        elif action == 'M2R':
            m1-=2;
            m2+=2;
            r='R';
        elif action == 'C1R':
            c1-=1;
            c2+=1;
            r='R';
        elif action == 'C2R':
            c1-=2;
            c2+=2;
            r='R';
        elif action == 'M1C1R':
            m1-=1;
            m2+=1;
            c1-=1;
            c2+=1;
            r='R';
        elif action == 'M1L':
            m1+=1;
            m2-=1;
            r='L';
        elif action == 'M2L':
            m1+=2;
            m2-=2;
            r='L';
        elif action == 'C1L':
            c1+=1;
            c2-=1;
            r='L';
        elif action == 'C2L':
            c1+=2;
            c2-=2;
            r='L';
        elif action == 'M1C1L':
            m1+=1;
            m2-=1;
            c1+=1;
            c2-=1;
            r='L';
        
        return (m1, m2, c1, c2, r)

    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        return state == (0,3,0,3,'R')

#-----------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Solve problem
result = depth_first(MissionariesAndCannibals(), graph_search=False)

# Print results
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'Goal achieved!')
    else:
        print('After moving', action)

    print(state)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------