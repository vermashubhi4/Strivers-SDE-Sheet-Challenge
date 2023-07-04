from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    # Write your code here.
    if not intervals:
        return intervals
    intervals.sort(key=lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end
    ans = []
    for i in range(1, len(intervals)):
        if(intervals[i].start<=end):
            end = max(end, intervals[i].end)
        else:
            obj = Solution(start, end)
            ans.append(obj)
            start = intervals[i].start
            end = intervals[i].end
    obj = Solution(start, end)
    ans.append(obj)
    return ans

    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
# arr1.sort()
# arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
