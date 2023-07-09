from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(arr) :
    # Write your code here.
    l=0
    mpp = {}
    ans = 0
    for r in range(len(arr)):
        if arr[r] in mpp:
            l = max(mpp[arr[r]]+1, l)
        mpp[arr[r]] = r
        ans = max(ans,r-l+1)
    return ans

