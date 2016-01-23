#divide and conquer solution for max subarray
#Written by Will Thomas

import time
import os
import csv
import sys

def max_subarray(array, start = 0, end=None):
     if end is None:
          end = len(array)
     if end == start:
          return start, end, array[start - 1]
     else:
          middle = (start + end) / 2

          leftLow, leftHigh, leftSum = max_subarray(array, start, middle)
          rightLow, rightHigh, rightSum = max_subarray(array, middle + 1, end)
          crossLow, crossHigh, crossSum = max_crossover(array, start, middle, end)

          if leftSum >= rightSum and leftSum >= crossSum:
               return leftLow, leftHigh, leftSum
          elif rightSum >= leftSum and rightSum >= crossSum:
               return rightLow, rightHigh, rightSum
          else:
               return crossLow, crossHigh, crossSum
          
def max_crossover(array, start, middle, end):
     currentLeftSum = 0
     leftSum = -sys.maxint - 1
     currentRightSum = 0
     rightSum = -sys.maxint - 1
     for i in range(middle, start, -1):
          currentLeftSum += array[i]
          if currentLeftSum > leftSum:
               leftsum = currentLeftSum
               leftIndex = i
     for i in range(middle, end):
          currentRightSum += array[i]
          if currentRightSum > rightSum:
               rightSum = currentRightSum
               rightIndex = i
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
                         leftIndex, rightIndex, result = max_subarray(row)
                         stopTime = time.clock()

                         resultTime = stopTime - startTime
                         
                         print("Largest Result: " + str(result))
                         print("Running Time: " + str(resultTime))

                         resultFile.write("\nArray: ")
                         for x in range(leftIndex, rightIndex + 1):
                              if (x > leftIndex):
                                   resultFile.write(", ")
                              resultFile.write(str(row[x]))

                         resultFile.write("\nMax sum: " + result)

main()
