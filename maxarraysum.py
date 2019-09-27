#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.


def maxSubsetSum(arr):
    max_sum = [0] * len(arr)

    for i in range(0, len(arr)):
        for j in range(0, len(arr), 2):
            if arr[i + j] >= 0:
                max_sum[i] += arr[i + j]

            if max_sum[i] < arr[i + j]:
                max_sum[i] = arr[i + j]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
