from math import *
from collections import *
from sys import *
from os import *

def subarraysXor(arr, k):
    # Write your code here
    # Return an integer
    xr = 0
    mpp = {}
    mpp[xr] = 1
    cnt = 0
    for el in arr:
        xr = xr ^ el
        x = xr ^ k
        cnt += mpp.get(x, 0)

        if mpp.get(xr):
            mpp[xr]+=1
        else:
            mpp[xr] = 1
    return cnt