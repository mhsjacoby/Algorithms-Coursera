## Course 3, Assignment 1, problem 2
## Scheduling algorithm using ration of weight/length (minimum)


import heapq
import heapq_max
import fractions
from heapq_max import *
from fractions import Fraction


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
		ratio = Fraction(weight, length)
		if ratio in jobs:
			jobCount += 1
			NumDuplicates = len(jobs[ratio])
			for L in range(0,NumDuplicates):
				if weight > jobs[ratio][L]['weight']:
					jobs[ratio].insert(L,newJob)
					break
			if len(jobs[ratio]) == NumDuplicates:
				jobs[ratio].append(newJob)
		else:
			jobs[ratio] = [newJob]

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

