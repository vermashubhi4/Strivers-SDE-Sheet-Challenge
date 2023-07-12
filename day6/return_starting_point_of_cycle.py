'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def firstNode(head):
    # Write your code here
    slow = head
    fast = head
    while slow and fast and fast.next and slow.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            break
    
    if not slow or not slow.next or slow != fast:
        return None
    
    fast = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow