#------------------------------------------------------------------------------------------------------------------
#   Logical programming library test
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from kanren import run, var, vars, eq, membero, Relation, facts, conde

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
    
# Define logical variable
x = var()

# ASK for 1 number, x, such that x == 5
# eq is a goal constructor to state that two expressions are equal
output = run(1, x, eq(x, 5))    
print('Result:', output)
    
# ASK for a number x such that x == z and z == 3
z = var()
output = run(1, x, eq(x, z), eq(z, 3))  
print('Result:', output)

# Ask for a number, x, such that (1, 2) == (1, x)
output = run(1, x, eq((1, 2), (1, x)))  
print('Result:', output)

# Ask for 2 values of x, such that x is a member of (1, 2, 3) and that x is a member of (2, 3, 4)
# membero(item, coll) states that item is a member of coll, a collection
output = run(2, x, membero(x, (1, 2, 3)),       # x is a member of (1, 2, 3)
            membero(x, (2, 3, 4)))              # x is a member of (2, 3, 4)
print('Result:', output)
    
# Define multiple logical variables
a, b, c = vars(3)
print (a, b, c)

# Define parent relation
parent = Relation()

# Define some facts about the parent relation
facts(parent, ("Omar", "Elisa"), ("Omar", "Amanda"), ("Javier",  "Omar"))

# Define goal constructor for grandparent relation
# conde, a goal constructor for logical and and or. 
# conde((A, B, C), (D, E)) means (A and B and C) or (D and E)
def grandparent(x, z):
    y = var()
    return conde((parent(x, y), parent(y, z)))  # x must be parent of y, and y must be parent of z
    
# Ask for Amanda's grandparent
output = run(2, x, grandparent(x, 'Amanda'))
print('Result:', output)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
