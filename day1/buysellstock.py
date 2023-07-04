from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    mp = 0
    buy = prices[0]
    n = len(prices)
    for i in range(1,n):
        buy = min(buy, prices[i])
        mp = max(mp, prices[i]-buy)
    return mp
