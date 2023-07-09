from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    arr.sort()
    low = 0
    high = len(arr)-1
    ans = []
    while(low<high):
        # print(low, high)
        if arr[low]+arr[high] == s:
            # print("equal")
            # high-=1
            # low+=1
            left = low
            right = high
            while(left<right and arr[left] + arr[right]==s):
                ans.append([arr[left], arr[right]])
                right-=1
            low+=1
        elif arr[low]+arr[high]<s:
            # print("less")
            low+=1
        else:
            # print("more")
            high-=1
    return ans