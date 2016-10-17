# Write a program that implements the following disk-scheduling algorithms:
# a. FCFS -fifo
# b. SSTF - sortest path to next head movement
# c. SCAN - scan to zero and then back up - given start head location
# d. C-SCAN - scan to end of disk then back down - given start head location
# e. LOOK - 
# f. C-LOOK
#  Your program will service a disk with 5,000 cylinders numbered 0 to 4,999. The program will generate a random 
# series of 1,000 cylinder requests and service them according to each of the algorithms listed above. The 
# program will be passed the initial position of the disk head (as a parameter on the command line) and report 
# the total amount of head movement required by each algorithm.

#HOW TO TURN IN
#source code, screenshot of executed code, results, strategy, 

import random
#import sys
#import os
import numpy

i = 0
cylinder = 4999
block = 512
request = []

#print out the average head movement for each algorithm, store each run in a temp
FSCSheadMov = []
SSTFheadMov = []

startHead = raw_input("Enter the start head position: ")
startHead = int(startHead)


#input several request for disk access
def getSchedule():
	request.append(startHead)
	while(len(request) < 10):
		request.append(random.randint(0,cylinder))
	return request

#First Come First Serve Algorithm 
def FCFS(scheduling):
	j = 1
	for access in scheduling:
		if( j <= len(scheduling)):
			headMov = abs(access - (scheduling[j]))
			FSCSheadMov.append(headMov)

			j += 1

#Shortest Seek Time First Algorithm
def SSTF(scheduling):
	minDist = []
	leftDis = 0
	rightDis = 0

	numpy.sort(scheduling)
	headPos = scheduling.index(startHead)

	for x in range(len(scheduling)):

		leftDis = abs(scheduling[headPos]) - scheduling[headPos-1]
		rightDis = abs(scheduling[headPos] - scheduling[headPos + 1])

		#number right of headmovement in arry is smallest dist
		if(leftDis < rightDis):
			headPos = scheduling[headPos-1]
			minDist.append(leftDis)
		elif(leftDis > rightDis):
			headPos = scheduling[headPos+1]
			minDist.append(rightDis)
		else()





while(i < 10):
	request = getSchedule
	print("request " + str(i) + " made")
	print(request)
	print("head movement " + str(i) + " between each request")
	print(headMovement)
	print("")
	request = []
	headMovement = []
	i += 1