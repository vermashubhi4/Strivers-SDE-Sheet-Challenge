from os import *
from sys import *
from collections import *
from math import *

def swap(arr, n, i):
    for index in range(n-1, i, -1):
        if arr[index]>arr[i-1]:
            return index
    return i

def reverse(arr, n, i):
    low = i
    high = n-1
    mid = (low+high)//2
    arr[low], arr[high] = arr[high], arr[low]
    low+=1
    high-=1
    while(low<=mid):
        arr[low], arr[high] = arr[high], arr[low]
        low+=1
        high-=1

def nextPermutation(arr, n):
    # Write your code here.
    # Return a list.
    
    for i in range(n-1, 0, -1):
        if(arr[i]>arr[i-1]):
            index = swap(arr, n, i)
            arr[index], arr[i-1] = arr[i-1], arr[index]
            # print("after swapping", arr)
            # if index!=i:
            reverse(arr, n, i)
                # print("after reversing", arr)
            return arr
    reverse(arr, n, 0)
    # print("after reversing reversed array", arr)
    return arr
