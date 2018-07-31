"""
uva 11507
Entradas:
	L:			Largo del tubo
	L-1			decisiones

"""
#Esta función debe de regresar la posición final.
def decide(decisiones,pos):
	for i in decisiones:
		if i[0] == "N":
			continue
		#En todas las x, se conserva el nuevo eje
		#El signo se invierte si x es negativa.
		if pos[1] == "x":
			pos[1] = i[1]
			if pos[0] == "-":
				if i[0] == "-":
					pos[0] = "+"
				else:
					pos[0] = "-"
			else:
				pos[0] = i[0]
			
		
		
		elif pos[1] == "y":
			pos[1] = chr(ord(i[1])-1) #ord
			if i[1] == "z":
			 	continue
			 #Si los signos son diferentes
			 #signo -> +
			 #si no: signo -> -
			elif i[1] == "y":
				if i[0] == pos[0]:
					pos[0] = "-"
				else:
					pos[0] = "+"
		
		elif pos[1] == "z":
			#Con y no cambia
			if i[1] == "y":
				continue
			elif i[1] == "z":
				pos[1] = "x"
				if pos[0] == i[0]:
					pos[0] = "-"
				else:
					pos[0] = "+"
	return pos

while True:
	L = int(input())
	if L == 0:
		break
	decisiones = input().split()
	#posición inicial
	pos = ["+","x"]
	#Mutamos el arreglo para que tenga el mismo formato
	#que la posición
	for idx, decision in enumerate(decisiones):
		decisiones[idx] = [decision[0],decision[1]]
	pos = decide(decisiones,pos)
	print("".join(pos))




