# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:

    def reversePortion(self, root) :
        head = None
        tail = None

        ptr = root
        while ptr :
            ptr2 = ptr.next
            ptr.next = None
            if head is None :
                head = ptr
                tail = ptr
            else :
                ptr.next = head
                head = ptr
            ptr = ptr2
        
        return head, tail


    def findLength(self, head) :
        ptr = head
        l = 0
        while ptr :
            ptr = ptr.next
            l += 1
        return l


	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):

        n = self.findLength(A)
        req_index = n//2 + n%2

        i = 1
        ptr = A
        while i < req_index :
            i += 1
            ptr = ptr.next
        
        head2 = ptr.next
        ptr.next = None
        
        head2, tail2 = self.reversePortion(head2)
        head1 = A

        ptr1 = head1
        ptr2 = head2
        while ptr2 :
            node = ptr2
            ptr2 = ptr2.next
            node.next = None

            node.next = ptr1.next
            ptr1.next = node
            ptr1 = node.next
        
        return head1

