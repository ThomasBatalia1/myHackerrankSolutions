#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    status = "" # string we will change depending on the result of the if statements
if (n % 2 == 1): #checks if n is odd
    status = "Weird"
elif ( n < 6 and n > 1): #check if n is in the inclusive range [2,5] 
    status = "Not Weird"
elif ( n > 20): # checks if n is greater than 20 
    status = "Not Weird"
elif ( n > 5 and n < 21): # checks if n is in the inclusive range [6,20]
    status = "Weird"
print(status)
