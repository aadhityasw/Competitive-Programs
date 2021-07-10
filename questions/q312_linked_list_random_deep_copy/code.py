# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None



class Solution:

    def processRandomPointer(self, head) :
        ptr = head

        if ptr not in self.table :
            new_ptr = RandomListNode(ptr.label)
            self.table[ptr] = new_ptr

        new_ptr = self.table[ptr]
        if ptr.random is None :
            new_ptr.random = None
        elif ptr.random in self.table :
            new_ptr.random = self.table[ptr.random]
        else :
            new_node = RandomListNode(ptr.random.label)
            new_ptr.random = new_node
            self.table[ptr.random] = new_node
            self.processRandomPointer(ptr.random)


    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        self.table = {}

        new_head = None
        new_tail = None

        ptr = head
        while ptr :
            self.processRandomPointer(ptr)
            ptr = ptr.next
        
        ptr = head
        while ptr :

            new_ptr = self.table[ptr]
            if new_head is None :
                new_head = new_ptr
                new_tail = new_ptr
            else :
                new_tail.next = new_ptr
                new_tail = new_ptr

            ptr = ptr.next

        return new_head
