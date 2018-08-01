"""
Entradas:
	T:		# de casos de prueba.
	N:		Número de piedras.
	D:		Distancia de orlla a orilla

	N piedras:
	Una linea con N piedras:
		S: Tamaño de la piedra
		M: Distancia de la orilla izquierda a la piedra.

"""

T = int(input())
for i in range(T):
	N, D = [int(x) for x in input().split()]
	piedras = input().split()
	for j in piedras:
		j = [x for x in j.split("-")]
		j[1] = int(j[1])
	for j in piedras:
		











