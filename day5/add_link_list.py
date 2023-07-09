class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    head3 = None
    temp1 = head1
    temp2 = head2
    carry = 0
    temp3 = None
    while temp1 and temp2:
        add_ = temp1.data + temp2.data + carry
        
        sum_ = add_%10
        if add_>9:
            carry = 1
        else:
            carry = 0
        temp_node = Node(sum_)
        if not head3:
            head3 = temp_node
            temp3 = head3
        else:
            temp3.next=temp_node
            temp3=temp3.next
        temp1 = temp1.next
        temp2 = temp2.next

    while temp1:
        add_ = temp1.data + carry
        sum_ = add_%10
        if add_>9:
            carry = 1
        else:
            carry = 0
        temp_node = Node(sum_)
        if not head3:
            head3 = temp_node
            temp3 = head3
        else:
            temp3.next=temp_node
            temp3=temp3.next
        temp1 = temp1.next
    while temp2:
        add_ = temp2.data + carry
        sum_ = add_%10
        if add_>9:
            carry = 1
        else:
            carry = 0
        temp_node = Node(sum_)
        if not head3:
            head3 = temp_node
            temp3 = head3
        else:
            temp3.next=temp_node
            temp3=temp3.next
        temp2 = temp2.next
    if carry!=0:
        temp_node = Node(carry)
        temp3.next=temp_node
        temp3=temp3.next
    return head3