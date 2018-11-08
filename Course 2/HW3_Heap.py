## Course 2, Assignment 3 - Using a Heap data structure
	
	# The goal of this problem is to implement the "Median Maintenance" algorithm 
	# (covered in the Week 3 lecture on heap applications). 
	# The text file contains a list of the integers from 1 to 10000 in unsorted order; 
	# you should treat this as a stream of numbers, arriving one by one. 
	# Letting xi denote the ith number of the file, the kth median mk is defined as 
	# the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th 
	# smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

	# In the box below you should type the sum of these 10000 medians, 
	# modulo 10000 (i.e., only the last 4 digits). 


import heapq
import heapq_max
from heapq_max import *

MyList = []
with open("Median_HW3.txt", "r") as f:
	for line in f:
		x = int(line.rstrip())
		MyList.append(x)

Heap_low = []   
heapq_max.heapify_max(Heap_low)            

Heap_high = []
heapq.heapify(Heap_high)

heapq.heappush(Heap_high, MyList[0])
heapq_max.heappush_max(Heap_low,MyList[1])


M = 6331 + 2793

for x in MyList[2:]:
	if x >= Heap_high[0]:
		heapq.heappush(Heap_high,x)
	else:
		heapq_max.heappush_max(Heap_low,x)
	combined_len = len(Heap_low) + len(Heap_high)
	if combined_len % 2 == 0:
		if len(Heap_high) > len(Heap_low):
			popped_h = heapq.heappop(Heap_high)
			heapq_max.heappush_max(Heap_low, popped_h)
		if len(Heap_high) < len(Heap_low):
			popped_l = 	heapq_max.heappop_max(Heap_low)
			heapq.heappush(Heap_high,popped_l)	
		m_k = Heap_low[0]
	elif len(Heap_high) > len(Heap_low):
		m_k = Heap_high[0]
	else:
		m_k = Heap_low[0]
	M = M + m_k		


print(len(Heap_low))
print(len(Heap_high))
print("M",M)
M_mod = M % 10000
print("M_mod", M_mod)					
