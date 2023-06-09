#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    count = 0 #I believe Int and Long were unified in python in a prior version. So nothing special should be required for this assignment
    for i in range(0,len(ar)): #iterates over the array and adds the values together
        count += ar[i] 
    OUTPUT_PATH = count #Returns the final count 
    return OUTPUT_PATH
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
