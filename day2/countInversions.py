from os import *
from sys import *
from collections import *
from math import *

def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid+1
    count = 0
    while(i<=mid and j<=high):
        if(arr[i]<=arr[j]):
            temp.append(arr[i])
            i+=1
        else:
            count+= (mid-i+1)
            temp.append(arr[j])
            j+=1
    while(i<=mid):
        temp.append(arr[i])
        i+=1
    while(j<=high):
        temp.append(arr[j])
        j+=1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    return count
    
def merge_sort(arr, low, high):
    count = 0
    if (low>=high):
      return count
    mid = floor((low+high)/2)
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count

def getInversions(arr, n) :
	# Write your code here.
	return merge_sort(arr, 0, n-1) 

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, input().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))