from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    hs = set()
    for num in arr:
        hs.add(num)
    # print(hs)
    ans = 1
    for num in arr:
        if num-1 not in hs:
            curr_num = num
            curr_streak = 1
            # print(curr_num, curr_streak)
            while curr_num+1 in hs:
                curr_num = curr_num+1
                curr_streak += 1
            ans = max(ans, curr_streak)
    return ans
