from math import *
from collections import *
from sys import *
from os import *

# Following is the class structure of the Node class:   
class Node:
    def __init__(self, data):
       	self.data = data
        self.next = None

def getListAfterReverseOperation(head, n, b):
    # Write your code here.
        dum = Node(0)
        dum.next = head
        prev = dum
        curr = dum
        nex = dum
        count= 0 
        while curr.next!=None:
            count+=1
            curr = curr.next
        j = 0
        while( j< len(b) and count >=b[j] ):
            if b[j]==0:
                j+=1
                continue
            if b[j]<2:
                j+=1
                prev = prev.next
                continue
            curr = prev.next
            nex = curr.next
            for i in range(1, b[j]):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count-=b[j]
            j+=1
        if (prev!=None and prev.next!=None and j< len(b) and b[j] > count):
            curr = prev.next
            nex = curr.next
            while(nex and curr):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next

        return dum.next
