
def reverse(head, k):
    
    if head.next is None :
        return head
    
    ptr = head
    ptr2 = head.next
    count = k-1
    
    while count > 0 and ptr2 is not None :
        ptr3 = ptr2.next
        ptr2.next = ptr
        head.next = ptr3
        ptr = ptr2
        ptr2 = ptr3
        count -= 1
        
    if head.next is not None :
        head.next = reverse(head.next, k)
    
    return ptr
        

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
