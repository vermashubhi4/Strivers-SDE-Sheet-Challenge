from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Write your code here.
	el = -1
	count = 0
	for elm in arr:
		if count==0:
			el = elm
			count=1
		elif elm == el:
			count+=1
		else:
			count-=1
	cnt = 0
	for elm in arr:
		if elm==el:
			cnt+=1
	if cnt>n//2:
		return el
	return -1