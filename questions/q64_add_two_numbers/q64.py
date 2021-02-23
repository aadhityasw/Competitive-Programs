# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()
        ptr = head
        ptr1 = l1
        ptr2 = l2
        carry = 0
        while (ptr1 and ptr2) :
            summ = ptr1.val + ptr2.val + carry
            carry = summ // 10
            summ = summ % 10

            node = ListNode(summ)
            ptr.next = node
            ptr = node

            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        if ptr1 :
            rem = ptr1
        else :
            rem = ptr2
        while (rem) :
            summ = rem.val + carry
            carry = summ // 10
            summ = summ % 10

            node = ListNode(summ)
            ptr.next = node
            ptr = node

            rem = rem.next
        
        # If there is a carry during the addition of MSD terms
        if carry :
            node = ListNode(carry)
            ptr.next = node
            ptr = node
        
        # To remove the dummy head placed before
        ptr = head
        head = head.next
        ptr.next = None
        ptr = None

        return head
