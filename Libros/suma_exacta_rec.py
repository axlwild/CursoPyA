
"""
Suma exacta
UVa 11057

"""


"""
Entradas:
	N:		Cantidad de libros disponibles.
	N 		enteros en cada línea
	M:		Dinero de Peter
"""
import sys
sys.setrecursionlimit(1000001)

#Función recursiva.
#Suponemos que entran los libros ordenados de manera ascendente.
def sumaExacta(libros,M,libros_elegidos):
	#Si hay menos de dos libros, ya no hay de dónde elegir nuevos libros.
	if len(libros) < 2:
		return libros_elegidos
	#Calculamos la suma del primer y último libro
	cuenta_aux = libros[0] + libros[-1]
	#Caso en el que cuestan más que lo que tiene -> Tenemos que elegir un libro con menor precio.
	if cuenta_aux > M:
		libros_elegidos = sumaExacta(libros[:-1],M,libros_elegidos)
	#Caso en el que cuestan menos que lo que tiene -> Tenemos que elegir un libro con mayor precio.
	elif cuenta_aux < M:
		libros_elegidos = sumaExacta(libros[1:],M,libros_elegidos)
	#Caso en el que coinciden los precios.
	elif cuenta_aux == M:
		libros_elegidos = [libros[0],libros[-1]]
		#Es posible que existan otros libros con menor diferencia.
		libros_elegidos = sumaExacta(libros[1:-1],M,libros_elegidos)
	
	return libros_elegidos

	

while True:
	try:			
		N 	   = int(input())
		libros = [int(x) for x in input().split()]
		M 	   = int(input())
		libros.sort()
		libros_elegidos = sumaExacta(libros,M,[])
		print("Peter should buy books whose prices are {} and {}.\n".format(libros_elegidos[0],libros_elegidos[1]))
		#Espacio en blanco de fin de prueba
		input()
	except EOFError :
		break





