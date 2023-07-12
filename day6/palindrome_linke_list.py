from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    
    # Write your code here.
    if not head or head.next==None:
        return True
    slow = head
    fast = head
    while(fast and fast.next!=None and fast.next.next!=None):
        slow = slow.next
        fast = fast.next.next
    
    slow2 = slow
    dum = head
    slow.next = reverseLinkedList(slow.next)
    slow=slow.next
    while slow != None:
        if slow.data != dum.data:
            return False
        slow =  slow.next
        dum = dum.next
    return True
    
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

    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head







#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
