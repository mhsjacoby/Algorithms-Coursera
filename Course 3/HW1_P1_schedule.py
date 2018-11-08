
## Course 3, Assinment 1, problem 1
## Scheduling job using minimum difference 

import heapq
import heapq_max
from heapq_max import *


jobs = {}
lineCount = 0
jobCount = 0
with open("alljobsHW1.txt", "r") as f:
	x = str.split(f.readline().strip())
	NumJobs = int(x[0])
	for line in f:
		lineCount += 1
		x = str.split(line)
		weight = int(x[0])
		length = int(x[1])
		newJob = {'weight': weight, 'length':length}
		diff = weight - length

		if diff in jobs:
			jobCount += 1
			NumDuplicates = len(jobs[diff])
			for L in range(0,NumDuplicates):
				if weight > jobs[diff][L]['weight']:
					jobs[diff].insert(L,newJob)
					break
			if len(jobs[diff]) == NumDuplicates:
				jobs[diff].append(newJob)
		else:
			jobs[diff] = [newJob]


M = 0
CompletionTime = 0
TotalWeightedTimes = 0
CurrentWeightedTime = 0

print("num duplicates", jobCount)
print("num unique Jobs", len(jobs))

k = 0
j = 0
for elem in range(0,len(jobs)):
 	M = max(jobs)
 	for i in range(0,len(jobs[M])):
 		k += 1
		CompletionTime = jobs[M][i]['length'] + CompletionTime
		CurrentWeightedTime = jobs[M][i]['weight'] * CompletionTime
 		TotalWeightedTimes = TotalWeightedTimes + CurrentWeightedTime
 	jobs.pop(M)

print(TotalWeightedTimes)
print("k", k)

