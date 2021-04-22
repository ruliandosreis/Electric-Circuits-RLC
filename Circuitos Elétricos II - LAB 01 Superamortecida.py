# LABORATÓRIO DE CIRCUITOS ELÉTRICOS II
# ANÁLISE DE CIRCUITOS RLC - CASO SUPERAMORTECIDO
# Rulian Dos Reis Fontes Novais
# 20/04/2021

# BIBLIOTECAS
import math
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# DEFININDO O ARRANJO DE T
t = np.arange(0, 5e-1, 1e-4) # tempo de amostragem entre 0 e 1 milisegundo com intervalo de 1 microsegundos

# DEFININDO VALORES DE R, L E C 
R = 25 # ohms
L = 0.25 # Henry
C = 2.5e-3 #microFaradays
V = 150 # Volts
Alfa = R/(2*L) 
Omega = 1/math.sqrt(L*C) 
Beta = math.sqrt(abs(Alfa**2 - Omega**2))

#expressão de i(t) obtida pelos cálculos realizados com o auxilio da transformada de Laplace 
it =  np.array([])
for i in t:
    it = np.append(it, (V/(2*L*Beta))*math.exp(-(Alfa-Beta)*i) - (V/(2*L*Beta))*math.exp(-(Alfa+Beta)*i))

#expressão de vc(t) obtida pelos cálculos realizados com o auxilio da transformada de Laplace
vct = np.array([])
for i in t:
    vct = np.append(vct, (V/(L*C*(Alfa**2 - Beta**2))) + (V/(L*C*((2*(Beta**2)) + (2*Alfa*Beta))))*math.exp(-(Alfa+Beta)*i) + (V/(L*C*(2*(Beta**2) - (2*Alfa*Beta))))*math.exp(-(Alfa-Beta)*i))

# PLOTAGEM DOS GRÁFICOS
fig, ax1 = plt.subplots(2, 1)

ax1[0].plot(t, it, 'r-', linewidth=2)
ax1[0].set_xlabel("Tempo(s)")
ax1[0].set_ylabel("Corrente (i)")
ax1[0].grid(True)
ax1[0].set_xlim(0,5e-1)
ax1[0].set_title('Resposta superamortecida da Corrente')

ax1[1].plot(t, vct, 'b-', linewidth=2)
ax1[1].set_xlabel("Tempo(s)")
ax1[1].set_ylabel("Tensão (V)")
ax1[1].grid(True)
ax1[1].set_xlim(0,5e-1)
ax1[1].set_title('Resposta superamortecida da Tensão')

fig.tight_layout()

plt.show()

#endcode