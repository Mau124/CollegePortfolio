#------------------------------------------------------------------------------------------------------------------
#   Prime test
#
#   This code is an adaptation of the family tree example described in:
#   Artificial intelligence with Python. Alberto Artasanchez and Prateek Joshi. 2nd edition, 2020, 
#   editorial Pack. Chapter 9.
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

import json
from kanren import Relation, facts, run, conde, var, eq
from kanren.core import success, fail

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
    
# Define relations
father = Relation()
mother = Relation()
    
# Open family member file)
with open('relationships.json') as f:
    d = json.loads(f.read())

# Set facts
for item in d['father']:
    facts(father, (list(item.keys())[0], list(item.values())[0]))

for item in d['mother']:
    facts(mother, (list(item.keys())[0], list(item.values())[0]))

# Define functions that test family relations
def parent(x, y):
    """ Check if 'x' is the parent of 'y'. """
    return conde([father(x, y)], [mother(x, y)])

def grandparent(x, y):
    """ Check if 'x' is the grandparent of 'y' """
    temp = var()
    return conde((parent(x, temp), parent(temp, y)))

def sibling(x, y):
    """ Check for sibling relationship between 'a' and 'b' """
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

def uncle(x, y):
    """ Check if x is y's uncle """
    temp = var()
    return conde((father(temp, x), grandparent(temp, y)))

def cousin(x, y):
    """ Check if x is y's cousin"""
    temp = var()
    return conde((uncle(temp, x), parent(temp, y)))
        
# Ron's children
x = var()
name = 'Ron'
output = run(0, x, father(name, x))
print("\nPregunta 1")
print("List of " + name + "'s children:")
for item in output:
    print(item)

# Dominique's mother
name = 'Dominique'
output = run(0, x, mother(x, name))[0]
print("\nPregunta 2")
print(name + "'s mother:\n" + output)

# Adam's parents 
name = 'Harry'
output = run(0, x, parent(x, name))
print("\nPregunta 3")
print("List of " + name + "'s parents:")
for item in output:
    print(item)

# Albus's grandparents 
name = 'Albus'
output = run(0, x, grandparent(x, name))
print("\nPregunta 4")
print("List of " + name + "'s grandparents:")
for item in output:
    print(item)

# Molly's grandchildren 
name = 'Molly'
output = run(0, x, grandparent(name, x))
print("\nPregunta 5")
print("List of " + name + "'s grandchildren:")
for item in output:
    print(item)

# Louis's siblings 
name = 'Louis'
output = run(0, x, sibling(x, name))
siblings = [x for x in output if x != name]
print("\nPregunta 6")
print("List of " + name + "'s siblings:")
for item in siblings:
    print(item)

# Lucy's uncles
name = 'Lucy'
name_father = run(0, x, father(x, name))[0]
output = run(0, x, uncle(x, name))
output = [x for x in output if x != name_father]
print("\nPregunta 7")
print("List of " + name + "'s uncles:")
for item in output:
    print(item)

# James Jr's cousins
name = 'James Jr'
siblings = list(run(0, x, sibling(x, name)))
cousins = list(run(0, x, cousin(x, name)))

for sibling in siblings:
    cousins.remove(sibling)

print("\nPregunta 8")
print("List of " + name + "'s cousins:")
for item in cousins:
    print(item)


# Fred Jr's uncle
temp = var()
name = 'Fred Jr'
output = list(run(0, x, uncle(x, name)))

print("\nPregunta 9")
print("List of " + name + "'s uncle:")
for item in output:
    print(item)

# All spouses
a, b, c = var(), var(), var()
output = run(0, (a, b), (father, a, c), (mother, b, c))
print("\nPregunta 10")
print("List of all spouses:")
for item in output:
    print('Husband:', item[0], '<==> Wife:', item[1])
     

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------