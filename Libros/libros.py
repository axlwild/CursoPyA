"""
UVA 11057

N:	numero de libros que va a comprar
L:	precio de libros
M:	dinero con el que cuenta

"""
import sys

while True:
	try:
		N = int(input())
		L = [int(x) for x in input().split()]
		m = int(input())
		input()

	except EOFError:
		break

	L.sort()

	i = 0
	j = N - 1
	a,b = 0,0
	while i < j:
		if(L[i] + L[j] < m):
			i += 1
		elif(L[i] + L[j] == m):
			a = i
			b = j
			i += 1
			j -= 1
		else:
			j -= 1

	print("Peter should buy books whose prices are %d and %d." % (L[a],L[]))
	print()











