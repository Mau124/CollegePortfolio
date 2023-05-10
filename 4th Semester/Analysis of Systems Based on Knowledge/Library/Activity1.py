from utils import *
from logic import *

# Create symbols for A figure
(A, B, C, D, E, Smoke, Fire, Heat) =  symbols("A, B, C, D, E, Smoke, Fire, Heat")

# 1. 
print("1")
print(tt_entails(A&B, A|'<=>'|B))

# 2. 
print("2")
print(tt_entails(A|'<=>'|B, A | B))

# 3. 
print("3")
print(tt_entails(A|'<=>'|B, ~A | B))

# 4. 
print("4")
print(tt_entails((A & B)|'==>'|C, (A|'==>'|C) | (B|'==>'|C)))

# 5. 
print("5")
print(tt_entails((A | B) & (~C | ~D | E), (A | C)))

# 6.
print("6")
print(tt_entails((A|B) & (~C | ~D | E), (A | B ) & (~D | E)))    

# 7.
print("7")
print(dpll_satisfiable((A | B) & ~(A|'==>'|B)))

# 8. 
print("8")
print(dpll_satisfiable((A|'<=>'|B) & (~A | B)))

# 9
print("9")
print(dpll_satisfiable((Smoke|'==>'|Fire)|'==>'|(~Smoke|'==>'|~Fire) ))

# 10
print("10")
print(dpll_satisfiable( ((Smoke & Heat)|'==>'|Fire)|'<=>'|((Smoke|'==>'|Fire) | (Heat|'==>'|Fire)) ) )