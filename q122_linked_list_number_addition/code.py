def addTwoLists(first, second):

    first = reverseList(first)
    second = reverseList(second)

    head = Node(0)
    carry = 0
    ptr = head

    while (first is not None) and (second is not None) :
        summ = first.data + second.data + carry
        carry = summ // 10
        summ = summ % 10

        ptr2 = Node(summ)
        ptr.next = ptr2
        ptr = ptr2

        first = first.next
        second = second.next
    
    if first is None :
        remaining = second
    else :
        remaining = first
    
    while remaining is not None :
        summ = remaining.data + carry
        carry = summ // 10
        summ = summ % 10

        ptr2 = Node(summ)
        ptr.next = ptr2
        ptr = ptr2

        remaining = remaining.next
    
    if carry > 0 :
        ptr2 = Node(carry)
        ptr.next = ptr2
        ptr = ptr2
    
    head = head.next
    head = reverseList(head)

    return head


def reverseList(head) :
    ptr = head

    while ptr.next is not None :
        ptr2 = ptr.next
        ptr.next = ptr2.next
        ptr2.next = head
        head = ptr2
    
    return head



# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addTwoLists(LL1.head, LL2.head)
        printList(res)
