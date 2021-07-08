# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):

        ptr1 = A
        ptr2 = A

        while ptr1 and ptr2 and ptr2.next :
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 is ptr2 :
                break
        
        #print(ptr1.val, ptr2.val)
        
        if ptr1 is None or ptr2 is None or ptr2.next is None :
            return None
        
        node_in_cycle = ptr1

        ptr1 = A
        ptr2 = node_in_cycle
        while ptr1 is not ptr2 :
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1
