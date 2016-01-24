#divide and conquer solution for max subarray
#Written by Will Thomas

import time
import os
import csv
import sys

def max_subarray(array, start = 0, end=None):
     #provide initial value for end
     if end is None:
          end = len(array)-1
     
     #Base case. If there is only 1 value left in array
     if end == start:
          return start, end, array[start]
     else:
          middle = (start + end) / 2
          
          #We have to get values for left side, right side, and middle where they cross over, then compare
          leftLow, leftHigh, leftSum = max_subarray(array, start, middle)
          rightLow, rightHigh, rightSum = max_subarray(array, middle + 1, end)
          crossLow, crossHigh, crossSum = max_crossover(array, start, middle, end)

          #Return array indices and sum of the solution
          if leftSum >= rightSum and leftSum >= crossSum:
               resultArray = [leftLow, leftHigh, leftSum]
               return resultArray
          elif rightSum >= leftSum and rightSum >= crossSum:
               resultArray = [rightLow, rightHigh, rightSum]
               return resultArray
          else:
               resultArray = [crossLow, crossHigh, crossSum]
               return resultArray
          
def max_crossover(array, start, middle, end):
     currentLeftSum = 0
     leftSum = -sys.maxint - 1
     currentRightSum = 0
     rightSum = -sys.maxint - 1
     leftIndex = middle
     rightIndex = middle+1

     #For the crossover range we have to find the values for everything
     #including the middle value
     for i in range(middle, start-1, -1):
          currentLeftSum += array[i]
          if currentLeftSum > leftSum:
               leftSum = currentLeftSum
               leftIndex = i
     for j in range(middle+1, end+1):
          currentRightSum += array[j]
          if currentRightSum > rightSum:
               rightSum = currentRightSum
               rightIndex = j
     return (leftIndex, rightIndex, leftSum + rightSum)

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
                         result = max_subarray(row)
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
