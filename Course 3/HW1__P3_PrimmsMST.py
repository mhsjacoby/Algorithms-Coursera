## Course 3, Assignment 1, problem 3
## Compute a minimum spanning tree using primms algorithm

V = {}
MaxCost = 0
with open("PrimmsDataHW1.txt", "r") as f:
#with open("MST_1.txt", "r") as f:
	f.next()
	for line in f:
		x = str.split(line)
		vertices = {}
		V1 = int(x[0])
		V2 = int(x[1])
		C = int(x[2])
		if C > MaxCost:
			MaxCost = C

		if V1 not in V:
			V[V1] = [{C:V2}]
		else: V[V1].append({C:V2})

		if V2 not in V:
			V[V2] = [{C:V1}]
		else: V[V2].append({C:V1})


X = [3]
TCost = 0
MinCost = MaxCost
temp = {0:0}

# display nodes and associated edges (edge cost is key, adjacent node is value)
# for vert in V:
# 	print(vert, V[vert])
# print("*****")	



while len(X) != len(V):
	MinCost = MaxCost
	for vert in X:
		sortedV = sorted(V[vert])
		for edge in sortedV:
			if edge.values()[0] not in X:
				if edge.keys()[0] <= MinCost:
					MinCost = edge.keys()[0]
					temp = edge
					break



	TCost = TCost + temp.keys()[0]
	X.append(temp.values()[0])

print(TCost)
