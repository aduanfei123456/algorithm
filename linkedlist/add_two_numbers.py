
"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
def add_two_numbers(node1,node2):
    sum=0
    head=Node(0)
    current=head
    while(node1 or node2):
        sum//=10
        if node1:
            sum+=node1.val
            node1=node1.next
        if node2:
            sum+=node2.val
            node2=node2.next
        current.next=Node(sum%10)
        current=current.next
    if(sum//10):
        current.next=Node(sum%10)
    return  head.next
node1=Node(2)
node1.next=Node(4)
node1.next.next=Node(3)
node2=Node(5)
node2.next=Node(6)
node2.next.next=Node(4)
node1=(add_two_numbers(node1,node2))
print(node1.val,node1.next.val,node1.next.next.val)