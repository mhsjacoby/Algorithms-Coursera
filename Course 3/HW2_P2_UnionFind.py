## Course 3, Assignment 2, problem 2
## Caclulate the hamming distance (number of differing bits) for bit represented graph
## determine the max number of clusers, K such that clusters are at least 3 bits apart



def Generate1DTests(node, n):
    test = ''
    for i in range(0,len(node)):
        if i == n:
            I = str(1 - int(node[i]))
        else:
            I = str(node[i])
        test = test + I  
    return(test);


def Generate2DTests(node, n, m):
    test = ''
    for i in range(0,len(node)):
        if i == n or i == m:
            I = str(1 - int(node[i]))
        else:
            I = str(node[i])
        test = test + I  
    return(test);

def UnionNodes(N1, N2):
    global Leaders
    global BitsDict

    Leader1 = BitsDict[N1]
    Leader2 = BitsDict[N2]
    ## figure out which is the larger and change only the smaller
    if len(Leaders[Leader1]) >= len(Leaders[Leader2]):
        NewLeader = Leader1
        OldLeader = Leader2
        BitsDict[N2] = NewLeader
    else:
        NewLeader = Leader2 
        OldLeader = Leader1 
        BitsDict[N1] = NewLeader

    NODES = []

    for x in range(0,len(Leaders[OldLeader])):
        node = Leaders[OldLeader][x]
        NODES.append(node)
        BitsDict[node] = NewLeader
        Leaders[NewLeader].append(node)

    for N in NODES:
        Leaders[OldLeader].remove(N)
      
    return Leaders;   


BitsDict = {} 
Leaders = {}
BitSet = set()


B = 0
with open("bitsData_HW2.txt", "r") as f:
#with open("test43_76.txt", "r") as f:
#with open("bitsTest1.txt", "r") as f:
    x = str.split(f.readline().strip())
    NumNodes = int(x[0])
    NumBits = int(x[1])
    for line in f:
        x = str.split(line)
        Bits = str(x[0])
        for i in x[1:]:
            Bits = Bits + str(i)
        BitsDict[Bits] = B
        Leaders[B] = [Bits]
        BitSet.add(Bits)
        B += 1


for B in BitsDict: 
    for n in range(0,len(B)):
        TEST = Generate1DTests(B,n)

        if TEST in BitsDict:
            if BitsDict[TEST] != BitsDict[B]:
                UnionNodes(TEST,B)

for B in BitsDict: 
    for n in range(0,len(B)):
        for m in range(0,len(B)):
            TEST = Generate2DTests(B,n,m)


            if TEST in BitsDict:
                if BitsDict[TEST] != BitsDict[B]:
                    UnionNodes(TEST,B)


## Calculate the number of clusters by counting the unique Leader names
ClusterSet = set()
for C in BitsDict:
    ClusterSet.add(BitsDict[C])
print(len(ClusterSet))