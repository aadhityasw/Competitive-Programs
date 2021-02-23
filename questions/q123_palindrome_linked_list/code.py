def isPalindrome(head):
    leng = 0
    ptr = head

    while ptr is not None :
        leng += 1
        ptr = ptr.next
    
    if leng == 1 :
        return True
    
    mid = head
    c = 1
    while c <= ((leng-1) // 2) :
        mid = mid.next
        c += 1
    
    if (leng % 2) == 1 :
        head2 = mid.next
    else :
        head2 = mid.next
        mid = mid.next
    
    head1 = head
    ptr = head1
    while ptr.next is not mid :
        ptr2 = ptr.next
        ptr.next = ptr2.next
        ptr2.next = head1
        head1 = ptr2
    ptr.next = None
    
    ptr1 = head1
    ptr2 = head2
    while (ptr1 is not None) and (ptr2 is not None) and (ptr1.data == ptr2.data) :
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    if ptr1 or ptr2 :
        return False
    else :
        return True
