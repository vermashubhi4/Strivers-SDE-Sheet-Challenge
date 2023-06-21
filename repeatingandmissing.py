from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    #find xor
    all_xor = 0
    for i in range(0,n):
        all_xor ^= arr[i]
        all_xor ^= (i+1)
    
    set_bit_num = all_xor & ~(all_xor-1)

    one = 0
    zero = 0
    for i in range(0, n):
        if(arr[i]&set_bit_num == 0):
            zero^=arr[i]
        else:
            one^=arr[i]
        if((i+1)&set_bit_num == 0):
            zero^=(i+1)
        else:
            one^=(i+1)
    count = 0
    for i in range(n):
        if zero == arr[i]:
            count+=1
    if count==2:
        return [one, zero]
    return [zero, one]