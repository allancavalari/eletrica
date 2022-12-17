#
# Cálculo de curto-circuito trifásico e monofásico em um sistema elétrico de potência
#
# Exemplo 4.16 (Blackburn 3ed)
#

from eletrica import *

#
# Dados do sistema
#

Sbase = 100 # MVA
Vbase = 115 # kV
Ibase_F = CorrenteBase(Sbase, Vbase) # A

V_G = Fasor("1<0")

#
# Impedâncias
#

j = complex(0,1)

Z_Ds = ZpuNovaBase(j*0.16, 80, 13.8, Sbase, 13.8)
Z_TG = ZpuNovaBase(j*0.11, 80, 13.8, Sbase, 13.8)
Z_LGH_12 = Zpu(j*24, Sbase, 115)

Z_TR_HM = ZpuNovaBase(j*5.5/100, 150, 230, Sbase, 230)
Z_TR_HL = ZpuNovaBase(j*36/100, 150, 230, Sbase, 230)
Z_TR_ML = ZpuNovaBase(j*28/100, 150, 230, Sbase, 230)

Z_H = 1/2*(Z_TR_HM+Z_TR_HL-Z_TR_ML)
Z_M = 1/2*(Z_TR_HM+Z_TR_ML-Z_TR_HL)
Z_L = 1/2*(Z_TR_HL+Z_TR_ML-Z_TR_HM)

Z_SIS_12 = j*3/100
Z_SIS_0 = j*4/100

Z_LGH_0 = Zpu(j*82, Sbase, 115)

Z1_G_12 = Paralelo(Z_Ds + Z_TG, Z_LGH_12 + Z_TR_HM + Z_SIS_12)

Z1, Z2 = Z1_G_12, Z1_G_12

Z0_G = Paralelo(Z_TG, Z_LGH_0+Z_M+Paralelo(Z_L, Z_H+Z_SIS_0))

#
# Cálculo das correntes de curto-circuito
#

I_3F_pu = Icc3f(V_G, Z1_G_12, 0)[1,0]

I_3F = I_3F_pu*Ibase_F

#
# Contribuições das barras G e H (divisor de corrente)
#

I_3F_G = Ibase_F*I_3F_pu*(Z_LGH_12 + Z_TR_HM + Z_SIS_12)/(Z_Ds + Z_TG + Z_LGH_12 + Z_TR_HM + Z_SIS_12)
I_3F_H = Ibase_F*I_3F_pu*(Z_Ds + Z_TG)/(Z_Ds + Z_TG + Z_LGH_12 + Z_TR_HM + Z_SIS_12)

I_AF_FT_pu = Icc1f(V_G, Z0_G, Z1, Z2, 0)
I_AF_FT = I_AF_FT_pu*Ibase_F

Icc1f_A = Fases(I_AF_FT)

#
# Output
#

print("> Corrente para falta trifásica na barra G:")
print(" I_3F (G):", I_3F.polar, "A")

print("> Contribuições das barras G e H para a falta trifásica na barra G:")

print(" I_3F (G<G):", I_3F_G.polar, "A")
print(" I_3F (G<H):", I_3F_H.polar, "A")

print("> Corrente para falta monofásica na fase A da barra G:")
print("IG_A:", Icc1f_A[0,0].polar , "A")
print("IG_B:", Icc1f_A[1,0].polar , "A")
print("IG_C:", Icc1f_A[2,0].polar , "A")
