def removeLoop(head):
    ptr = head
    ptr2 = head
    
    while True :
        if ptr is None or ptr2 is None or ptr2.next is None :
            return
        ptr = ptr.next
        ptr2 = ptr2.next.next
        if ptr is ptr2 :
            loopNode = ptr
            break
    
    ptr = loopNode.next
    count = 1
    while ptr is not loopNode :
        ptr = ptr.next
        count += 1
    
    
    ptr = head
    ptr1 = head
    ptr2 = head.next
    while count > 1 :
        ptr2 = ptr2.next
        ptr1 = ptr1.next
        count -= 1
    
    
    while ptr is not ptr2 :
        ptr = ptr.next
        ptr2 = ptr2.next
        ptr1 = ptr1.next
    
    ptr1.next = None
