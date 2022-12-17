#
# Aplicação: Curto-circuito bifásico nos terminais de um gerador síncrono entre as fases B-C (Ia=0, Vb=Vc, Ib+Ic=0)
#
# Sn=30MVA; Vbase=13.8kV; Xd''=X1=0.2pu; X2=0.25pu; X0=0.08pu; Xgnd=0.09pu
#
# Exemplo 6.5.1 (Curto-circuito - Geraldo Kindermann)
#

from eletrica import *

#
# Parâmetros
#

Ea = Fasor("1<90")

Z1 = Impedancia("j0.20")
Z2 = Impedancia("j0.25")

Zf = 0

# Base

Sn = 30e6
Vbase = 13.8e3
Ibase = Sn/((3**0.5)*Vbase)

#
# Cálculo da corrente de curto-circuito bifásico (Ia1=-Ia2, Ia0=0)
#

If = Icc2f(Ea, Z1, Z2, 0)

#
# Cálculo das correntes reais nas fases A, B e C
#

Iabc = Fases(If)*Ibase

#
# Tensão das fases do gerador
#

Ia0, Ia1, Ia2 = If[0][0], If[1][0], If[2][0]

Va0 = 0
Va1 = Ea - Z1*Ia1
Va2 = Va1

V012 = Vetor012(Va0, Va1, Va2)

Vabc = Fases(V012)*Vbase/3**0.5

#
# Output
#

print("> Correntes das fases para curto-circuito bifásico nas fases B-C:")
print("I_A:", Iabc[0,0].polar , "A")
print("I_B:", Iabc[1,0].polar , "A")
print("I_C:", Iabc[2,0].polar , "A")

print("> Tensão das fases do gerador para curto-circuito bifásico nas fases B-C:")
print("V_AN:", (1/1000*Vabc[0,0]).polar , "kV")
print("V_BN:", (1/1000*Vabc[1,0]).polar , "kV")
print("V_CN:", (1/1000*Vabc[2,0]).polar , "kV")
