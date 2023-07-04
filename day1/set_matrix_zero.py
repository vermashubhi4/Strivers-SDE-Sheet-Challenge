from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    set_row = 0
    set_col = 0

    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

                if i == 0:
                    set_row = 1
                if j == 0:
                    set_col = 1
        
    for i in range(1, n):
        for j in range(1, m):
            if matrix[0][j] ==0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if set_row:
        for i in range(0, m):
            matrix[0][i] = 0
    if set_col:
        for j in range(0, n):
            matrix[j][0] = 0
