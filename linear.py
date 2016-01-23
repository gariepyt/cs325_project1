# Linear for max sub array
# Written by: Tom Gariepy

# Import
import time
import os
import csv
import sys

# Where the linear search is implemented
def linearSearch(array):
	curStart = 0
	curStop = 0
	curSum = 0

	maxStart = 0
	maxStop = 0
	maxSum = 0
	for x in range(0, len(array)):
		if (array[x] > curSum + array[x]):
		# if (max(array[x], curSum + array[x]) == array[x]):
			curSum = array[x]
			curStart = x
			curStop = x
		else:
			curSum = curSum + array[x]
			curStop = x

		if (curSum > maxSum):
		# if (max(curSum, maxSum) == curSums):
			maxSum = curSum
			maxStart = curStart
			maxStop = curStop

	resultArray = [maxStart, maxStop, maxSum]
	return resultArray

	# return maxSum

def main():
	
	# rfname = "MSS_TestProblems.txt"
	rfname = "MSS_Problems.txt"
	wfname = "MSS_Results.txt"

	# Check to see if file exists
	fileCheck = os.path.isfile(rfname)
	if (fileCheck == False):
		print("ERROR: " + rfname + " not found.")
		return 1

	print("Program running")

	# Create 
	with open(wfname, 'wt') as resultFile:	

		# Open the file and read each line by line
		with open(rfname, 'rt') as fileArr:
		# print ("File opened")
			fStream = csv.reader(fileArr)
			for row in fStream:
				if (len(row) > 0): 
					row[0] = row[0].replace('[', '')
					row[len(row) - 1] = row[len(row) - 1].replace(']', '')
				
					row = list(map(int, row))

					# For testing
					# print(row)

					startTime = time.clock()
					result = linearSearch(row)
					stopTime = time.clock()

					resultTime = stopTime - startTime

					print("Largest Result: " + str(result[2]))
					print("Running Time: " + str(resultTime))

					resultFile.write("Array: ")
					for x in range(result[0], result[1] + 1):
						if (x > result[0]):
							resultFile.write(", ")
						resultFile.write(str(row[x]))

					resultFile.write("\nMax sum: " + str(result[2]) + "\n")

main()
#print (sys.version)