from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	cnt1 = 0
	cnt2 = 0
	el1 = 0
	el2 = 0
	n = len(arr)
	for el in arr:
		if cnt1==0 and el2!=el:
			cnt1=1
			el1=el
		elif cnt2==0 and el1!=el:
			cnt2=1
			el2=el
		elif el==el1:
			cnt1+=1
		elif el==el2:
			cnt2+=1
		else:
			cnt1-=1
			cnt2-=1
	c1 = 0
	c2 = 0
	for el in arr:
		if el==el1:
			c1+=1
		elif el == el2:
			c2+=1
	ans = []
	if c1 > n//3:
		ans.append(el1)
	if c2 > n//3:
		ans.append(el2)
	return ans