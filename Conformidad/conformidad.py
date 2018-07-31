







"""
Entradas:
	n:			Número de alumnos.
	clases: 	clases que toma cada alumno
"""

while True:	
	claves = {}
	n = int(input())
	if n == 0 :
		break
	"""
	Valida si existe la clave. y se aumenta su valor
	por cada vez que se repita.
	"""
	for i in range(n):
		clases = input().split()
		clases.sort()
		aux = "".join(clases)
		if aux in claves:
			claves[aux] += 1
		else:
			claves[aux] = 1
	maximo = max(claves.values())
	alumnos = 0
	#Buscamos las claves que son máximas
	for i in claves:
		if claves[i] == maximo:
			alumnos += maximo
	print(alumnos)












