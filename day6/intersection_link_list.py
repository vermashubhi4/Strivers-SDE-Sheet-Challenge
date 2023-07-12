'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(head1, head2):
	# Write your code here.
    if not head1 or not head2:
        return None
    d1 = head1
    d2 = head2
    while d1!=d2:
        d1 = head2 if not d1 else d1.next
        d2 = head1 if not d2 else d2.next
    return d1
