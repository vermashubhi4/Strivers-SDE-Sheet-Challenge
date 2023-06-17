from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    ans = [[1]]
    if n==1:
        return ans
    ans.append([1,1])
    if n==2:
        return ans

    for row in range(2, n):
        temp = [1]
        for col in range(1,row):
            temp.append(ans[row-1][col-1] + ans[row-1][col])
        temp.append(1)
        ans.append(temp)
    return ans