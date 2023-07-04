from os import *
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    slow, fast = 0, 0
    slow = arr[slow]
    fast = arr[arr[fast]]
    while(slow!=fast):
        slow = arr[slow]
        fast = arr[arr[fast]]
    
    fast = 0
    while slow!=fast:
        slow = arr[slow]
        fast = arr[fast]
    return fast