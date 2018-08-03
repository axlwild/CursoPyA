
"""
Entradas:
	cad1:		Cadenas a comparar para obtener su lcs
	cad2:		Cadenas a comparar para obtener su lcs
"""
import sys
sys.setrecursionlimit(2000)
def subsecuencia(cad1,cad2,l1,l2):
	#Caso base
	if len(cad1)==0 or len(cad2) == 0:
		sol[l1][l2] = 0
	#Si no hemos calculado una solución 
	#De un par de subcadenas... Las calculamos
	if sol[l1][l2] == -1:
		if cad1[-1] == cad2[-1]:
			sol[l1][l2] = 1 + subsecuencia(cad1[:-1],cad2[:-1],l1-1,l2-1)
		else:
			sol[l1][l2] = max(subsecuencia(cad1,cad2[:-1],l1,l2-1),
				subsecuencia(cad1[:-1],cad2,l1-1,l2))
	return sol[l1][l2]


while True:
	try:
		cad1 = input()
		cad2 = input()
		#Matriz que guarda las soluciones que hemos calculado
		#anteormente
		sol = []
		for i in cad1+" ":
			#-1 significa que aun no encontramos la solución
			sol.append([-1]*(len(cad2)+1))
		#Saliendo de este ciclo queda una matriz
		#de (n+1)*(m+1)
		print(subsecuencia(cad1,cad2,len(cad1),len(cad2)))
	#En caso de que aparezca el fin del archivo, salimos.
	except EOFError:
		break

























