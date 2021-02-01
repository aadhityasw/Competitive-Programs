# This function should rotate list counter-
# clockwise by k and return head node
def rotate(head, k):
    count = 0
    ptr = head
    while ptr :
        count += 1
        ptr = ptr.next
    k = k % count
    
    new_head = head
    while k :
        new_head = new_head.next
        k -= 1
    
    tail = new_head
    while tail.next :
        tail = tail.next
    
    while head is not new_head :
        ptr = head
        head = head.next
        tail.next = ptr
        ptr.next = None
        tail = ptr
    
    return new_head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = rotate(lis.head,k)
        printList(head)
