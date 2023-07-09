'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    # Write your code here.
    # start.next = head
    slow = head
    fast = head

    for i in range(1, k+1):
        fast = fast.next

    while fast and fast.next!=None:
        slow = slow.next
        fast = fast.next

    if fast!=None:
        slow.next = slow.next.next
    else:
        head = head.next

    return head