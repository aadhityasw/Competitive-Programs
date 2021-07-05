class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def partition(self, A, B):

        head0 = None
        tail0 = None
        head1 = None
        tail1 = None

        ptr = A
        while ptr is not None :
            ptr2 = ptr.next
            ptr.next = None

            if ptr.val < B :
                if head0 is None :
                    head0 = ptr
                    tail0 = ptr
                else :
                    tail0.next = ptr
                    tail0 = ptr
            else :
                if head1 is None :
                    head1 = ptr
                    tail1 = ptr
                else :
                    tail1.next = ptr
                    tail1 = ptr

            ptr = ptr2

        if tail0 is not None :
            tail0.next = head1
        return head0 if head0 is not None else head1
