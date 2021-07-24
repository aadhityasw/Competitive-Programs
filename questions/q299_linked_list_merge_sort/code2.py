class Solution:
    
    def mergeLists(self, A, B) :
        
        ptr1 = A
        ptr2 = B
        head = None
        tail = None
        
        while ptr1 and ptr2 :
            if ptr1.data < ptr2.data :
                node = ptr1
                ptr1 = ptr1.next
            else :
                node = ptr2
                ptr2 = ptr2.next
            node.next = None
            if head is None :
                head = node
                tail = node
            else :
                tail.next = node
                tail = node
        
        if ptr1 :
            if head :
                tail.next = ptr1
            else :
                head = ptr1
        if ptr2 :
            if head :
                tail.next = ptr2
            else :
                head = ptr2
        
        return head
    
    
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        
        if head is None or head.next is None :
            return head
        
        ptr = head
        n = 0
        while ptr :
            ptr = ptr.next
            n += 1
        
        mid = head
        for i in range(n//2 - 1) :
            mid = mid.next
        
        B = mid.next
        mid.next = None
        A = head
        return self.mergeLists(self.mergeSort(A), self.mergeSort(B))
