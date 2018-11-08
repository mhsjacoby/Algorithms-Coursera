## Course 1, Assignment 2

	## This file contains all of the 100,000 integers between 1 and 100,000 
	## (inclusive) in some order, with no integer repeated.
	## Your task is to compute the number of inversions in the file given, 
	## Because of the large size of this array, 
	## you should implement the fast divide-and-conquer algorithm covered in the video lectures.



#global Count 
Count = 0


def sort(A):
	global Count 

	n = len(A)
	if n%2 == 0:
		m = n/2
	else:
		m = (n+1)/2	

	# Base Case
	if n == 1:
		Ans = (A)
		return Ans

	else:
		B = A[:m]
		B = sort(B)
		C = A[m:]
		C = sort(C)

		numLen = len(B) + len(C)
		D = []									# empty array for merged list

		i = 0									# index for B
		j = 0									# index for C
												
		for x in range(0,numLen):

			if i == len(B) and j < len(C):		# end of array B reached		
				D.append(C[j])					# add rest of C to D
				j += 1
				numJump = len(B)-i
				Count += numJump

			elif j == len(C) and i < len(B):	# end of array C reached
				D.append(B[i])					# add rest of B to D
				i += 1							
				#Count += j-i						# increment inverse count

			elif B[i] > C[j]:
				#print("B[i] > C[j]")
				D.append(C[j])
				j += 1
				numJump = len(B)-i
				Count += numJump
			else:
				#print("B[i] <= C[j]")
				D.append(B[i])
				i += 1
			#print("D",D)
			#print("Count", Count)
		#Count = Count + tempCount	
		return D	

	#print("out of the loop")

				

	#Count = Count + Count
	
		#print("finalCount",finalCount)
	#print("D",D)
	#print(D)
	#return	D



#Unsorted = [7,3,6,11,29,19,18,15,14,13,1000,-1,57,99,10,5,242,42,8,9,4,1]	
#Unsorted = [10,20,4,1,2,3,6,7,8]	

NumberList = []
lines = [line.rstrip('\r\n') for line in open("nums_HW2.txt")]
for x in range(0,len(lines)):
	NumberList.append(int(lines[x]))




#Count = 0
NewArray = []
inOrder = sort(NumberList)

print(NumberList)
print(inOrder)	
print(Count)




		