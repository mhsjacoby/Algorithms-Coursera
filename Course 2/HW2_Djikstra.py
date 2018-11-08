
## Course 2, Assignment 2 - Djikstra's shortest path algorithm

	## The file contains an adjacency list representation of an 
	## undirected weighted graph with 200 vertices labeled 1 to 200.
	## Each row consists of the node tuples that are adjacent to that 
	## particular vertex along with the length of that edge. 

	# For example, the 6th row has 6 as the first entry indicating that 
	# this row corresponds to the vertex labeled 6. 
	# The next entry of this row "141,8200" indicates that there is 
	# an edge between vertex 6 and vertex 141 that has length 8200. 
	# The rest of the pairs of this row indicate the other vertices adjacent to vertex 6
	#  and the lengths of the corresponding edges.

	# Your task is to run Dijkstra's shortest-path algorithm on this graph, 
	# using 1 (the first vertex) as the source vertex, and to compute the shortest-path 
	# distances between 1 and every other vertex of the graph. 
	# If there is no path between a vertex v and vertex 1, 
	# we'll define the shortest-path distance between 1 and v to be 1000000.




### Open/read file

Vspace = {}	
with open("DjikstraData_HW2.txt", "r") as f:
	for line in f:
		x = str.split(line)
		vertices = {}
		for v in x[1:]:
			vert = v.split(",")
			vertices[int(vert[0])] = int(vert[1])
		Vspace[int(x[0])] = vertices	
print(Vspace)		

X = {}
X[1] = 0
while len(X) != len(Vspace):
	minLen = 1000000
	minVert = 1
	for v in X:
		for w in Vspace[v]:
			if w not in X:
				if Vspace[v][w] + X[v] < minLen:
					minLen = Vspace[v][w] + X[v]
					minVert = w
	X[minVert] = minLen

print("7",X[7])
print("37",X[37])
print("59",X[59])
print("82",X[82])
print("99",X[99])
print("115",X[115])
print("133",X[133])
print("165",X[165])
print("188",X[188])
print("197",X[197])


## 7,37,59,82,99,115,133,165,188,197




