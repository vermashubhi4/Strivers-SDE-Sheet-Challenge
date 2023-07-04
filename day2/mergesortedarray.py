from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    arr3 =[]
    i, j = 0, 0
    while(i<m and j<n):
        if(arr1[i]<=arr2[j]):
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while(i<m):
        arr3.append(arr1[i])
        i+=1
    while(j<n):
        arr3.append(arr2[j])
        j+=1
    for i in range(len(arr3)):
        arr1[i] = arr3[i]
    return arr1
