#divide and conquer solution for max subarray
#Written by Will Thomas

import time
import os
import csv
import sys

# Used for algorithm #3, returns larges sum found between two arrays
def maxMiddleSum(array, low, mid, high):

  # Calculate max subarray on left side of current array
  sum = 0
  leftSum = 0
  for i in range(mid, low-1, -1):
    sum += array[i]
    if sum > leftSum:
      leftSum = sum

  # Calculate max subarray on right side of the current array
  sum = 0
  rightSum = 0
  for i in range(mid+1, high+1, 1):
    sum += array[i]
    if sum > rightSum:
      rightSum = sum

  return (leftSum + rightSum)

# Used for algorithm #3, returns maxSubArray sum
def maxSubArray(array, low, high):
  # BASE CASE
  if low == high:
    return array[low]
  mid = (low + high) / 2

  # Return the maximum of left sum, right sum, and combined(middle) sum
  return max(maxSubArray(array, low, mid), maxSubArray(array, mid+1, high),
      (maxMiddleSum(array, low, mid, high)))

def main():
     
     # rfname = "MSS_TestProblems.txt"
     rfname = "MSS_TestProblems-1.txt"
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
                         startTime = time.clock()
                         result = maxSubArray(row, 0, len(row)-1)
                         stopTime = time.clock()

                         resultTime = stopTime - startTime
                         
                         print("Largest Result: " + str(result))
                         print("Running Time: " + str(resultTime))

                         resultFile.write("\nMax sum: " + str(result))

main()
