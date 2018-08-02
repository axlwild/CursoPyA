"""
UVa 11389
El problema de los choferes de camión.
"""


"""
Entradas:
n:		Número de choferes/rutas matutinas y verpertinas.
d:		horas normales de trabajo del chofer.
r:		tasa de $ adicional por hora.
maxh:	número máximo de horas
"""
while True:
	n,d,r = [int(x) for x in input().split()]
	if n == d == r == 0:
		break
	maxh 	  = 0
	rutas_mat = [int(x) for x in input().split()]
	rutas_ves = [int(x) for x in input().split()]
	rutas_mat.sort()
	rutas_ves.sort(reverse=True)
	for i in range(n):
		horas = rutas_mat.pop() + rutas_ves.pop()
		if horas > d:
			maxh += horas - d
	print(maxh*r)








