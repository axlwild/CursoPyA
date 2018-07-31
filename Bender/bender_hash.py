


dicc = {}
dicc["+x+y"] = "+y"
dicc["+x-y"] = "-y"
dicc["+x+z"] = "+z"
dicc["+x-z"] = "-z"
dicc["-x+y"] = "-y"
dicc["-x-y"] = "+y"
dicc["-x+z"] = "-z"
dicc["-x-z"] = "+z"
dicc["+y+y"] = "-x"
dicc["+y-y"] = "+x"
dicc["+y+z"] = "+y"
dicc["+y-z"] = "+y"
dicc["-y+y"] = "+x"
dicc["-y-y"] = "-x"
dicc["-y+z"] = "-y"
dicc["-y-z"] = "-y"
dicc["+z+y"] = "+z"
dicc["+z-y"] = "+z"
dicc["+z+z"] = "-x"
dicc["+z-z"] = "+x"
dicc["-z+y"] = "-z"
dicc["-z-y"] = "-z"
dicc["-z+z"] = "+x"
dicc["-z-z"] = "-x"


while True:
	L = int(input())
	if L == 0:
		break
	decisiones = input().split()
	pos = "+x"
	for i in decisiones:
		if i == "No":
			continue
		else:
			pos = dicc[pos+i]
	print(pos)



