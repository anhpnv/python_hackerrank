#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
#1 w 2 r 3g
def solve(s):
    s = list(s)
    s[0] = s[0].capitalize()
    for i in range(len(s)):
        if s[i] == " ":
            s[i+1] = s[i+1].capitalize()
    return "".join(s) 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
