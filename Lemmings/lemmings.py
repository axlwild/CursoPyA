

"""
Entradas:
	N:			Número de casos de prueba.
	B:			Campos de batalla
	SG:			lemmings verdes
	SB:			lemmings azules

verdes: 	Lista con lemmings verdes.
azules:		Lista con lemmings azules.
"""

N = int(input())
for prueba in range(N):
	B, SG, SB = [int(x) for x in input().split()]
	verdes = []
	azules = []
	for lemverde in range(SG):
		verdes.append(int(input()))
	for lemazul in range(SB):
		azules.append(int(input()))

	while len(verdes) > 0 < len(azules):
		verdes.sort(reverse=True)
		azules.sort(reverse=True)
		#Contador para eliminar a los muertos de las listas (del ejército).
		muerte_azul = 0
		muerte_verde = 0
		#Batalla
		for i in range(B):
			#Si hay más campos de batalla que ejercito, salimos.
			if (len(verdes) < i + 1) or len(azules) < i+1 :
				break
			batalla = azules[i] - verdes[i]
			if batalla > 0:
				azules[i], verdes[i] = batalla, 0
				muerte_verde += 1
			elif batalla < 0:
				azules[i], verdes[i] = 0, -batalla
				muerte_azul += 1
			else:
				azules[i], verdes[i] = 0, 0
				muerte_azul += 1
				muerte_verde += 1
		#Aquí eliminamos a los muertos después de la pelea.
		for i in range(muerte_azul):
			azules.remove(0)
		for i in range(muerte_verde):
			verdes.remove(0)
	azules.sort(reverse=True)
	verdes.sort(reverse=True)
	#En este punto, un equipo se quedó sin ejército.
	if len(azules) > 0:
		print("blue wins")
		for i in azules:
			print(i)
	elif len(verdes) > 0:
		print("green wins")
		for i in verdes:
			print(i)
	else:
		print("green and blue died")
	print()









