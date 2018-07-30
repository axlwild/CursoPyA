"""
Entrada:
H:		Altura del pozo
U:		Avance
D:		Distancia que resbala
F:		Factor de fatiga


"""


while True:
	H,U,D,F = [float(x) for x in input().split()]
	if H==U==D==F==0:
		break
	dia = 0
	fatiga = F/100 *U
	avance_actual = U
	distancia = 0

	while 0 <= distancia  <= H:
		dia += 1
		if avance_actual > 0:
			distancia += avance_actual
		if distancia > H:
			print("success on day",dia)
			break
		distancia -= D
		if distancia < 0:
			print("failure on day",dia)
			break
		avance_actual = U - fatiga*dia
		#avance_actual -= fatiga












