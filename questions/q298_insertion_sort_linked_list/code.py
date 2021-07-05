# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def insertionSortList(self, A):

        head = A
        ptr = head.next
        tail = head
        tail.next = None

        while ptr is not None :
            ptr2 = ptr.next

            if ptr.val < head.val :
                ptr.next = head
                head = ptr
            elif ptr.val >= tail.val :
                tail.next = ptr
                ptr.next = None
                tail = ptr
            else :
                ptr3 = head
                while ptr3.next is not tail and ptr3.next.val <  ptr.val :
                    ptr3 = ptr3.next
                ptr.next = ptr3.next
                ptr3.next = ptr
            
            ptr = ptr2
            
        return head
