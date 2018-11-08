## Course 1, Assignment 4
# Minimum cut problem on adjacency list (graph)


	## The file contains the adjacency list representation of a simple undirected graph.
	## There are 200 vertices labeled 1 to 200.
	## Your task is to code up and run the randomized contraction algorithm for the 
	## min cut problem and use it on the above graph to compute the min cut. 
	## (HINT: Note that you'll have to figure out an implementation of edge contractions.)


import random
import csv
from copy import deepcopy

def MinCut(x):
	A = deepcopy(x)
	if len(A) < 3:
		numCuts = len(A[0])-1
		return numCuts

	else:
		u = random.randint(0,len(A)-1)
		a = A[u][0] #value(name) of first vertex
		b = random.choice(A[u][1:])	# value(name) of connecting vertex
		A[u] = filter(lambda v: v != b, A[u])
		B_index = 0

		for i in range(0,len(A)):
			if A[i][0] == b:
				A[i] = filter(lambda g: g!=a, A[i])
				B_index = i
				A[u].extend(A[i][1:])
			for j in range(1,len(A[i])):
				if A[i][j] == b:
					A[i][j] = a

		del A[B_index]
	return(MinCut(A))					


d = []

with open("GraphArray_HW4.txt") as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

for i in range(len(d)):
	n = len(d[i])-1
	for j in range(n):
		d[i][j] = int(d[i][j])
	del d[i][n]	

MinLen = len(d)	

for i in range(100):	
	D = deepcopy(d)
	C = MinCut(D)
	if C < MinLen:
		MinLen = C

print("min", MinLen)		

