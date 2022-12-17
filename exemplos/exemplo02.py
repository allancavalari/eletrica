#
# Aplicação: Curto-circuito trifásico nos terminais de um gerador síncrono (Va=Vb=Vc=0)
#
# Sn=30MVA; Vbase=13.8kV; Xd''=X1=0.2pu; X2=0.25pu; X0=0.08pu; Xgnd=0.09pu
#
# Exemplo 6.3.1 (Curto-circuito - Geraldo Kindermann)
#

from eletrica import *

#
# Parâmetros
#

Ea = Fasor("1<90")
Zg = Impedancia("j0.2")

# Base

Sn = 30e6
Vbase = 13.8e3
Ibase = Sn/((3**0.5)*Vbase)

#
# Cálculo da corrente de sequência positiva
#

If = Icc3f(Ea, Zg, 0)

#
# Cálculo das correntes reais nas fases A, B e C
#

Iabc = Fases(If)*Ibase

#
# Output
#

print("I_A:", Iabc[0,0].polar , "A")
print("I_B:", Iabc[1,0].polar , "A")
print("I_C:", Iabc[2,0].polar , "A")
