def sortedMerge(head_A, head_B):
    
    ptr2 = head_A
    temp_head = head_B
    head = head_A
    while (temp_head is not None) and (temp_head.data <= head.data) :
        ptr = temp_head
        temp_head = temp_head.next
        ptr.next = head
        head = ptr
    
    ptr = head
    while (ptr.next is not None) and (temp_head is not None) :
        if (ptr.next is not None) and (ptr.next.data >= temp_head.data) :
            ptr2 = temp_head
            temp_head = temp_head.next
            ptr2.next = ptr.next
            ptr.next = ptr2

        ptr = ptr.next
    
    if temp_head is not None :
        ptr.next = temp_head
    
    return head
