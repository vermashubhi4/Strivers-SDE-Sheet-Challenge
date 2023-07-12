class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.


def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    return flatten(head)

def flatten(root):
    if(root == None or root.next == None):
        return root
    root.next = flatten(root.next)
    root = mergeTwoLinkedLists(root, root.next)
    return root

def mergeTwoLinkedLists(l1, l2):
    temp = Node()
    res = temp
    while(l1!=None and l2!=None):
        if l1.data<l2.data:
            temp.child = l1
            temp = temp.child
            l1 = l1.child
        else:
            temp.child = l2
            temp = temp.child
            l2 = l2.child
    if l1!=None:
        temp.child = l1
    else:
        temp.child = l2
    return res.child
