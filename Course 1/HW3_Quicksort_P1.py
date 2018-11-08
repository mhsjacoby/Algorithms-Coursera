## Course 1, Assignment 3, problem 1 (of 3)


	## The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.
	## The integer in the ith row of the file gives you the ith entry of an input array.
	## Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. 
	## As you know, the number of comparisons depends on which elements are chosen as pivots, 
	## so we'll ask you to explore three different pivoting rules.
	## You should not count comparisons one-by-one. 
	## Rather, when there is a recursive call on a subarray of length m, 
	## you should simply add m−1 to your running total of comparisons.

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
		L = 0
		P = A[0]
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
lines = [line.rstrip('\r\n') for line in open("NumberList_HW3.txt")]
for x in range(0,len(lines)):
	NumberList.append(int(lines[x]))

inOrder = Quicksort(NumberList)

print(Comparison)




		

