#ENTRADAS

# T: NÚMERO DE CASOS
# L: LONGITUD DE LA BANDERA
# R: RADIO

import math

T = int(input())

for i in range(T):
	L=int(input())
	H=3*L/5
	R=(1/5)*L
	Ar=(R**2)*math.acos(-1)
	Av=(L*H)-Ar
	print('{:0.2f} {:0.2f}'.format(Ar,Av))