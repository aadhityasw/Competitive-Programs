def getNthFromLast(head,n):
    leng = 0
    ptr = head
    
    while ptr is not None :
        leng += 1
        ptr = ptr.next
    
    if n > leng :
        return -1
    
    k = leng - n
    ptr = head
    while k > 0 :
        ptr = ptr.next
        k -= 1
    
    return ptr.data
