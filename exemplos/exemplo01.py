#
# Cálculo da corrente em um circuito elétrico de corrente alternada
#

from eletrica import Fasor, Impedancia

#
# Tensão (V)
#

V = Fasor("100<0°")

#
# Impedância (Ω)
#

Z = Impedancia("1+j0.5")

#
# Corrente (A)
#

I = Fasor(V/Z)

#
# Output
#

print(I, "A")