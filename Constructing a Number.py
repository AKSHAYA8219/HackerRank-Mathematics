#!/bin/python3

import math
import os
import random
import re
import sys

def canConstruct(a):
    sum=0
    for i in a:
        while i:
            i, remainder = divmod(i, 10)
            sum += remainder

    #if the sum of all the digits in the number is divisible by 3. If so, the number itself must also be divisible by 3.
    if(sum%3==0):
        return("Yes")
    else:
        return("No")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
