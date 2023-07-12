'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    fast = head
    slow = head
    while slow and fast and slow.next and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False