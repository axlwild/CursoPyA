from heapq import *

N = int(input())

for i in range(N):
	B,SG,SB = [int(x) for x in input().split()]
	verdes=[]
	azules=[]
	for j in range(SG):
		verdes.append(-int(input()))
	for j in range(SB):
		azules.append(-int(input()))
	#Heapify "convierte" una lista en una cola de prioridad.
	heapify(azules)
	heapify(verdes)
	#Pelean mientras haya Lemmings en cada equipo.
	while len(azules) > 0 < len(verdes):
		#El ejército varía durante la batalla
		ganador_azul,ganador_verde = [], []
		long_azul,long_verde = len(azules),len(verdes)
		for k in range(B):
			if long_azul < k+1 or  long_verde < k+1 :
				break
			batalla = -heappop(azules) - -heappop(verdes)

			if batalla > 0:
				ganador_azul.append(-batalla)
			elif batalla < 0:
				ganador_verde.append(batalla)
		#Ya terminaron de pelear una ronda
		for k in ganador_azul:
			heappush(azules,k)
		for k in ganador_verde:
			heappush(verdes,k)
	#En este punto un equipo se quedó sin ejército.
	if len(azules) > 0:
		print("blue wins")
		while azules:
			print(-heappop(azules))
	elif len(verdes) > 0:
		print("green wins")
		while verdes:
			print(-heappop(verdes))
	else:
		print("green and blue died")
	if i != N-1:
		print()














		







