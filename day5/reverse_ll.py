from math import *
from collections import *
from sys import *
from os import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    # Write your code here.

    prev = None
    curr = head
    while(curr != None):
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev

