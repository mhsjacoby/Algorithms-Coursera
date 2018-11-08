## Course 1, Assignment 3, problem 2
## Quicksort of a numerical list - Recurrsion
	## Compute the number of comparisons (as in Problem 1), 
	## always using the final element of the given array as the pivot element.




Comparison = 0
def Quicksort(A):
	global Comparison
	n = len(A)
#	print(A)
	if n <= 1:
		return A
	else:
		# Choose partition to be left-most element of subarray
		Comparison = Comparison + n-1

		P = A[n-1]
		A[n-1] = A[0]
		A[0] = P

		L = 0
		R = n
		i = 1
		for j in range(L+1,R):
			if A[j] < P:
				temp = A[j]
				A[j] = A[i]
				A[i] = temp
				i += 1
		newI = A[L]
		A[L] = A[i-1]
		A[i-1] = newI
#		print(A)



		LEFT = A[:i-1]
		RIGHT = A[i:]

		LEFT = Quicksort(LEFT)
		RIGHT = Quicksort(RIGHT)

		A = LEFT + A[i-1:i] + RIGHT

	

		return A


#Unsorted = [7,3,6,11,29,19,18,15,14,13,1000,-1,57,99,10,5,242,42,8,9,4,1]	
#Unsorted = [3,10,13,5,20,4,1,6,19,2,8,7]	
#Unsorted = [6,2,9,4,3,5]


NumberList = []
lines = [line.rstrip('\r\n') for line in open("nums2.txt")]
for x in range(0,len(lines)):
	NumberList.append(int(lines[x]))


inOrder = Quicksort(NumberList)
	
print(Comparison)



		

