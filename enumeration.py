# Enumeration for Max Subarray
# Author: Jeffrey Schachtsick
# Last Update: 01/19/2015
# Description: Read from a single text file and output the enumeration for
#       a max subarray, while getting the system clock speed.

# Imports
import os
import time
import csv


def getPath():
    """ Verify MSS_TestProblems-1.txt is available. """
    valid = False
    file = "MSS_TestProblems-1.txt"
    if os.path.isfile(file):
        print("\nFile located...")
        valid = True
    else:
        print("\nThe file is not located")
    return valid

def enumerationMaxSubArray(array):
    """ This is the enumeration algorithm for Max Sub Array """
    maxSub = 0
    maxStart = 0
    maxStop = 0
    for i in range(0, len(array)):
        curStart = i
        for j in range(i, len(array)):
            cur = 0
            curStop = j
            for k in range(i, j + 1):
                cur += array[k]
                if cur > maxSub:
                    maxSub = cur
                    maxStart = curStart
                    maxStop = curStop
    resultArray = [maxStart, maxStop, maxSub]
    return resultArray

# Main
def main():
    """ Main management of all functions """
    # Variables
    file = "MSS_TestProblems-1.txt"

    # Make sure file is available
    valid = getPath()
    if (valid == False):
        return 0

    # Open the file, read each line into an array
    with open(file, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            row = list(map(int, row))

            # Start the clock
            start = time.clock()

            # Start the algorithm
            resultArray = enumerationMaxSubArray(row)

            # Stop the clock
            stop = time.clock()

            # Get the total clock
            totalTime = stop - start

            # parse result array
            for x in range(resultArray[0], resultArray[1] +1):
                if(x == resultArray[0]):
                    print "[",
                if (x > resultArray[0]):
                    print ", ",
                print row[x],
            print("]")

            # Print Max Sub Array
            print(resultArray[2])

            # Print total time
            print("Total system time for Enumeration Algorithm: ", totalTime)
            print("\n")

main()