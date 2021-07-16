


def swapkthnode(head,num,k):

    if num < k :
        return head
    
    if k > (num // 2) :
        k = num - k + 1
    
    if num%2 == 1 and k == (num//2 + num%2) :
        return head

    if k == 1 :
        if num == 1 :
            return head
        
        # Get last but one node
        ptr = head
        while ptr.next and ptr.next.next :
            ptr = ptr.next
        
        """ptr2 = head.next
        ptr3 = head
        head = ptr.next
        head.next = ptr2
        ptr.next = ptr3
        ptr3.next = None"""
        
        node1 = head
        node2 = ptr.next
        ptr.next = node1
        node2.next = head.next
        node1.next = None
        head = node2

        return head
    
    ptr1 = head
    ptr2 = head

    i = 1
    while i < k-1 and ptr1.next :
        ptr1 = ptr1.next
        i += 1
    
    i = 1
    while i < num-k and ptr2.next :
        ptr2 = ptr2.next
        i += 1

    node1 = ptr1.next
    node2 = ptr2.next
    
    if ptr2 is ptr1.next :
        node1.next = node2.next
        node2.next = node1
        ptr1.next = node2
        return head
    
    nextnode1 = node1.next
    nextnode2 = node2.next
    node1.next = nextnode2
    node2.next = nextnode1
    ptr1.next = node2
    ptr2.next = node1

    return head







import atexit
import io
import sys


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        new_head=swapkthnode(a.head,n, kth_node)

        new_check = [getNthfromEnd(new_head, kth_node), getNthfromBeg(new_head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)
