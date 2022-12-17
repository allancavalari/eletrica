#
# Aplicação: Curto-circuito monofásico no terminal da fase A de um gerador síncrono (Va=0, Ib=Ic=0)
#
# Sn=30MVA; Vbase=13.8kV; Xd''=X1=0.2pu; X2=0.25pu; X0=0.08pu; Xgnd=0.09pu
#
# Exemplo 6.4.1 (Curto-circuito - Geraldo Kindermann)
#

from eletrica import *

#
# Parâmetros
#

Ea = Fasor("1<90")

Zgnd = Impedancia("j0.09")

Z0 = Impedancia("j0.08")
Z1 = Impedancia("j0.20")
Z2 = Impedancia("j0.25")

Zf = 0

# Base

Sn = 30e6
Vbase = 13.8e3
Ibase = Sn/((3**0.5)*Vbase)

#
# Cálculo da corrente de curto-circuito monofásico (Ia0=Ia1=Ia2 e If=3*Ia1)
#

If = Icc1f(Ea, Z0 + 3*Zgnd, Z1, Z2, Zf)

#
# Cálculo das correntes reais nas fases A, B e C
#

Iabc = Fases(If)*Ibase

Ia0, Ia1, Ia2 = If[0][0], If[1][0], If[2][0]

Ibase = Sn/((3**0.5)*Vbase)

#
# Cálculo da corrente real no neutro
#

In = 3*Ia0*Ibase

#
# Tensão entre neutro do gerador e a terra
#

Vn = -3*Zgnd*Ia0*(Vbase/3**0.5)

#
# Tensões de sequência no defeito
#

V0 =  0 - Z0*Ia0
V1 = Ea - Z1*Ia1
V2 =  0 - Z2*Ia2

V012 = Vetor012(V0, V1, V2)

#
# Tensões de fase do gerador síncrono
#

Vabc = Fases(V012)*(Vbase/3**0.5)

#
# Output
#

print("> Correntes das fases no curto-circuito monofásico na fase A:")
print("I_A:", Iabc[0,0].polar , "A")
print("I_B:", Iabc[1,0].polar , "A")
print("I_C:", Iabc[2,0].polar , "A")

print("> Corrente no neutro do gerador:")
print("IN:", In.polar, "A")

print("> Tensão no neutro do gerador:")
print("VN:", Vn.polar, "V")

print("> Tensão das fases nos terminais do gerador:")
print("V_AN:", (1/1000*Vabc[0,0]).polar , "kV")
print("V_BN:", (1/1000*Vabc[1,0]).polar , "kV")
print("V_CN:", (1/1000*Vabc[2,0]).polar , "kV")

print("> Tensão entre as linhas:")
print("V_AB:", (1/1000*(Vabc[0,0] - Vabc[1,0])).polar , "kV")
print("V_BC:", (1/1000*(Vabc[1,0] - Vabc[2,0])).polar , "kV")
print("V_CA:", (1/1000*(Vabc[2,0] - Vabc[0,0])).polar , "kV")

#
# Tensões de sequência nos terminais do gerador
#

V0 =  0 - (Z0+3*Zgnd)*Ia0
V1 = Ea - Z1*Ia1
V2 =  0 - Z2*Ia2

V012 = Vetor012(V0, V1, V2)

#
# Tensões de fase nos terminais do gerador síncrono
#

Vabc = Fases(V012)*(Vbase/3**0.5)

#
# Output
#

print("> Tensão das fases nos terminais do gerador:")
print("V_AN:", (1/1000*Vabc[0,0]).polar , "kV")
print("V_BN:", (1/1000*Vabc[1,0]).polar , "kV")
print("V_CN:", (1/1000*Vabc[2,0]).polar , "kV")