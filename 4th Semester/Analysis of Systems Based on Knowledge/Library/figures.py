from utils import *
from logic import *

# Create symbols for A figure
(Ac, Ap, At, As, Am, Ag) =  symbols("Ac, Ap, At, As, Am, Ag")

# Create symbols for B figure
(Bc, Bp, Bt, Bs, Bm, Bg) =  symbols("Bc, Bp, Bt, Bs, Bm, Bg")

# Create symbols for C figure
(Cc, Cp, Ct, Cs, Cm, Cg) =  symbols("Cc, Cp, Ct, Cs, Cm, Cg")

# Create symbols for D figure
(Dc, Dp, Dt, Ds, Dm, Dg) =  symbols("Dc, Dp, Dt, Ds, Dm, Dg")

# Create symbols for E figure
(Ec, Ep, Et, Es, Em, Eg) =  symbols("Ec, Ep, Et, Es, Em, Eg")

# Create symbols for F figure
(Fc, Fp, Ft, Fs, Fm, Fg) =  symbols("Fc, Fp, Ft, Fs, Fm, Fg")

kb = PropKB()

# Tell what we now about the Kb

# Base conditions
kb.tell( (At & ~Ac & ~Ap) | (~At & Ac & ~Ap) | (~At & ~Ac & Ap) )
kb.tell( (Bt & ~Bc & ~Bp) | (~Bt & Bc & ~Bp) | (~Bt & ~Bc & Bp) )
kb.tell( (Ct & ~Cc & ~Cp) | (~Ct & Cc & ~Cp) | (~Ct & ~Cc & Cp) )
kb.tell( (Dt & ~Dc & ~Dp) | (~Dt & Dc & ~Dp) | (~Dt & ~Dc & Dp) )
kb.tell( (Et & ~Ec & ~Ep) | (~Et & Ec & ~Ep) | (~Et & ~Ec & Ep) )
kb.tell( (Ft & ~Fc & ~Fp) | (~Ft & Fc & ~Fp) | (~Ft & ~Fc & Fp) )

kb.tell( (As & ~Am & ~Ag) | (~As & Am & ~Ag) | (~As & ~Am & Ag) )
kb.tell( (Bs & ~Bm & ~Bg) | (~Bs & Bm & ~Bg) | (~Bs & ~Bm & Bg) )
kb.tell( (Cs & ~Cm & ~Cg) | (~Cs & Cm & ~Cg) | (~Cs & ~Cm & Cg) )
kb.tell( (Ds & ~Dm & ~Dg) | (~Ds & Dm & ~Dg) | (~Ds & ~Dm & Dg) )
kb.tell( (Es & ~Em & ~Eg) | (~Es & Em & ~Eg) | (~Es & ~Em & Eg) )
kb.tell( (Fs & ~Fm & ~Fg) | (~Fs & Fm & ~Fg) | (~Fs & ~Fm & Fg) )

# Propositions
kb.tell(At |'==>'| Bt)
kb.tell(Bt |'==>'| Ct)
kb.tell( (At & Ct) |'==>'| (Ag | Cg) )
kb.tell(At)
kb.tell(~Cg)
kb.tell( (Cs & Dp) |'==>'| Dm)
kb.tell( Cm |'==>'| (~Dc & ~Ec & ~Fc) )
kb.tell( ~As|'==>'|(Dp & Ds) )
kb.tell( Eg|'==>'| (Dg|'<=>'|Fg))
kb.tell( (Ds & Es) | (Dm & Em) | (Dg & Eg) )
kb.tell( (Dc & Ec) | (Dp & Ep) | (Dt & Et) )
kb.tell( Fg|'==>'|((Fc | Fp)))
kb.tell(( (Cg & Em) | (Cg & Es) | (Cm & Es)) |'==>'| ((Bg & Cm) | (Bg & Cs) | (Bm & Cs)) )

# DPLL 
kb_string = ""
for elem in kb.clauses:
    elem = to_cnf(str(elem))
    kb_string = kb_string + str(elem) + " & "

#########################################################################################
#
#                                       Figure A
#
#########################################################################################

# Test At -> A is triangle
alpha = kb_string + str(to_cnf(str( ~At )))
print("A es triangulo: " +  ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True" ))

# Test ~At -> A is not a triangle
alpha = kb_string + str(to_cnf(str( At )))
print("A no es triangulo: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Ac -> A is an square
alpha = kb_string + str(to_cnf(str( ~Ac )))
print("A es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Ac -> A is not a square
alpha = kb_string + str(to_cnf(str( Ac )))
print("A no es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Ap -> A is a pentagon
alpha = kb_string + str(to_cnf(str( ~Ap )))
print("A es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Ap -> A is not a pentagon
alpha = kb_string + str(to_cnf(str( Ap )))
print("A no es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Size A
#
#########################################################################################

# Test As -> A is small
alpha = kb_string + str(to_cnf(str( ~As )))
print("A es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~As -> A is not small
alpha = kb_string + str(to_cnf(str( As )))
print("A no es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Am -> A is medium
alpha = kb_string + str(to_cnf(str( ~Am )))
print("A es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Am -> A is not medium
alpha = kb_string + str(to_cnf(str( Am )))
print("A no es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Ag -> A is big
alpha = kb_string + str(to_cnf(str( ~Ag )))
print("A es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Ag -> A is not big
alpha = kb_string + str(to_cnf(str( Ag )))
print("A no es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Figure B
#
#########################################################################################

# Test Bt -> B is triangle
alpha = kb_string + str(to_cnf(str( ~Bt )))
print("B es triangulo: " +  ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True" ))

# Test ~Bt -> B is not a triangle
alpha = kb_string + str(to_cnf(str( Bt )))
print("B no es triangulo: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Bc -> B is an square
alpha = kb_string + str(to_cnf(str( ~Bc )))
print("B es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Bc -> B is not a square
alpha = kb_string + str(to_cnf(str( Bc )))
print("B no es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Bp -> B is a pentagon
alpha = kb_string + str(to_cnf(str( ~Bp )))
print("B es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Bp -> B is not a pentagon
alpha = kb_string + str(to_cnf(str( Bp )))
print("B no es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Size B
#
#########################################################################################

# Test Bs -> B is small
alpha = kb_string + str(to_cnf(str( ~Bs )))
print("B es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Bs -> B is not small
alpha = kb_string + str(to_cnf(str( Bs )))
print("B no es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Bm -> B is medium
alpha = kb_string + str(to_cnf(str( ~Bm )))
print("B es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Bm -> B is not medium
alpha = kb_string + str(to_cnf(str( Bm )))
print("B no es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Bg -> B is big
alpha = kb_string + str(to_cnf(str( ~Bg )))
print("B es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Bg -> B is not big
alpha = kb_string + str(to_cnf(str( Bg )))
print("B no es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Figure C
#
#########################################################################################

# Test Ct -> C is triangle
alpha = kb_string + str(to_cnf(str( ~Ct )))
print("C es triangulo: " +  ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True" ))

# Test ~Ct -> C is not a triangle
alpha = kb_string + str(to_cnf(str( Ct )))
print("C no es triangulo: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Cc -> C is an square
alpha = kb_string + str(to_cnf(str( ~Cc )))
print("C es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Cc -> C is not a square
alpha = kb_string + str(to_cnf(str( Cc )))
print("C no es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Cp -> C is a pentagon
alpha = kb_string + str(to_cnf(str( ~Cp )))
print("C es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Cp -> C is not a pentagon
alpha = kb_string + str(to_cnf(str( Cp )))
print("C no es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Size C
#
#########################################################################################

# Test Cs -> C is small
alpha = kb_string + str(to_cnf(str( ~Cs )))
print("C es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Cs -> C is not small
alpha = kb_string + str(to_cnf(str( Cs )))
print("C no es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Cm -> C is medium
alpha = kb_string + str(to_cnf(str( ~Cm )))
print("C es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Cm -> C is not medium
alpha = kb_string + str(to_cnf(str( Cm )))
print("C no es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Cg -> C is big
alpha = kb_string + str(to_cnf(str( ~Cg )))
print("C es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Cg -> C is not big
alpha = kb_string + str(to_cnf(str( Cg )))
print("C no es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Figure D
#
#########################################################################################

# Test Dt -> D is triangle
alpha = kb_string + str(to_cnf(str( ~Dt )))
print("D es triangulo: " +  ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True" ))

# Test ~Dt -> D is not a triangle
alpha = kb_string + str(to_cnf(str( Dt )))
print("D no es triangulo: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Dc -> D is an square
alpha = kb_string + str(to_cnf(str( ~Dc )))
print("D es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Dc -> D is not a square
alpha = kb_string + str(to_cnf(str( Dc )))
print("D no es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Dp -> D is a pentagon
alpha = kb_string + str(to_cnf(str( ~Dp )))
print("D es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Dp -> D is not a pentagon
alpha = kb_string + str(to_cnf(str( Dp )))
print("D no es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Size D
#
#########################################################################################

# Test Ds -> D is small
alpha = kb_string + str(to_cnf(str( ~Ds )))
print("D es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Ds -> D is not small
alpha = kb_string + str(to_cnf(str( Ds )))
print("D no es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Dm -> D is medium
alpha = kb_string + str(to_cnf(str( ~Dm )))
print("D es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Dm -> D is not medium
alpha = kb_string + str(to_cnf(str( Dm )))
print("D no es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Dg -> D is big
alpha = kb_string + str(to_cnf(str( ~Dg )))
print("D es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Dg -> D is not big
alpha = kb_string + str(to_cnf(str( Dg )))
print("D no es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Figure E
#
#########################################################################################

# Test Et -> E is triangle
alpha = kb_string + str(to_cnf(str( ~Et )))
print("E es triangulo: " +  ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True" ))

# Test ~Et -> E is not a triangle
alpha = kb_string + str(to_cnf(str( Et )))
print("E no es triangulo: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Ec -> E is an square
alpha = kb_string + str(to_cnf(str( ~Ec )))
print("E es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Ec -> E is not a square
alpha = kb_string + str(to_cnf(str( Ec )))
print("E no es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Ep -> E is a pentagon
alpha = kb_string + str(to_cnf(str( ~Ep )))
print("E es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Ep -> E is not a pentagon
alpha = kb_string + str(to_cnf(str( Ep )))
print("E no es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Size E
#
#########################################################################################

# Test Es -> E is small
alpha = kb_string + str(to_cnf(str( ~Es )))
print("E es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Es -> E is not small
alpha = kb_string + str(to_cnf(str( Es )))
print("E no es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Em -> E is medium
alpha = kb_string + str(to_cnf(str( ~Em )))
print("E es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Em -> E is not medium
alpha = kb_string + str(to_cnf(str( Em )))
print("E no es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Eg -> E is big
alpha = kb_string + str(to_cnf(str( ~Eg )))
print("E es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Eg -> E is not big
alpha = kb_string + str(to_cnf(str( Eg )))
print("E no es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Figure F
#
#########################################################################################

# Test Ft -> F is triangle
alpha = kb_string + str(to_cnf(str( ~Ft )))
print("F es triangulo: " +  ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True" ))

# Test ~Ft -> F is not a triangle
alpha = kb_string + str(to_cnf(str( Ft )))
print("F no es triangulo: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Fc -> F is an square
alpha = kb_string + str(to_cnf(str( ~Fc )))
print("F es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Fc -> F is not a square
alpha = kb_string + str(to_cnf(str( Fc )))
print("F no es cuadrado: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Fp -> F is a pentagon
alpha = kb_string + str(to_cnf(str( ~Fp )))
print("F es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Fp -> F is not a pentagon
alpha = kb_string + str(to_cnf(str( Fp )))
print("F no es pentagono: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

#########################################################################################
#
#                                       Size F
#
#########################################################################################

# Test Fs -> F is small
alpha = kb_string + str(to_cnf(str( ~Fs )))
print("F es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Fs -> F is not small
alpha = kb_string + str(to_cnf(str( Fs )))
print("F no es chico: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Fm -> F is medium
alpha = kb_string + str(to_cnf(str( ~Fm )))
print("F es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Fm -> F is not medium
alpha = kb_string + str(to_cnf(str( Fm )))
print("F no es mediano: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()

# Test Fg -> F is big
alpha = kb_string + str(to_cnf(str( ~Fg )))
print("F es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))

# Test ~Fg -> F is not big
alpha = kb_string + str(to_cnf(str( Fg )))
print("F no es grande: " + ("False" if isinstance(dpll_satisfiable(expr(alpha)), bool) else "True"))
print()