from math import *
from collections import *
from sys import *
from os import *

def rotateMatrix(arr, n, m):

    # Write your code here
    start_row = 0
    start_col = 0
    end_row = n-1
    end_col = m-1

    while(start_row<end_row and start_col<end_col):
        #right
        prev = arr[start_row][start_col]
        for i in range(start_col+1, end_col+1):
            nxt = arr[start_row][i]
            arr[start_row][i] = prev
            prev = nxt
        #down
        for j in range(start_row+1, end_row+1):
            nxt = arr[j][end_col]
            arr[j][end_col] = prev
            prev = nxt
        
        #left
        for i in range(end_col-1, start_col-1, -1):
            nxt = arr[end_row][i]
            arr[end_row][i] = prev
            prev = nxt
        
        #up
        for j in range(end_row-1, start_row-1, -1):
            nxt = arr[j][start_col]
            arr[j][start_col] = prev
            prev = nxt
        start_row+=1
        end_row-=1
        start_col+=1
        end_col-=1
