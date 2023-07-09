from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    hm = {}
    ans = 0
    sum_ = 0
    for i in range(len(arr)):
        sum_+= arr[i]
        if sum_==0:
            ans = i+1
        else:
            if sum_ in hm:
                ans = max(ans, i-hm[sum_])
            else:
                hm[sum_] = i
    return ans