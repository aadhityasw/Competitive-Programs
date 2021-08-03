# Node Class    
class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    k=0
    for _ in range(n):
        lis.insert(arr[k], arr[k+1])
        k+=2
    return lis.head









class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        
        head = None
        tail = None
        ptr1 = poly1
        ptr2 = poly2
        
        while ptr1 and ptr2 :
            if ptr1.power < ptr2.power :
                cur_node = node(ptr2.coef, ptr2.power)
                ptr2 = ptr2.next
            elif ptr1.power > ptr2.power :
                cur_node = node(ptr1.coef, ptr1.power)
                ptr1 = ptr1.next
            else :
                cur_node = node(ptr1.coef + ptr2.coef, ptr1.power)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            
            if head :
                tail.next = cur_node
                tail = cur_node
            else :
                head = cur_node
                tail = cur_node
        
        if ptr1 :
            cur_node = ptr1
        elif ptr2 :
            cur_node = ptr2
        else :
            cur_node = None
        if head :
            tail.next = cur_node
        else :
            head = cur_node
        
        return head
        
        
        
        
        
        
        
        
        

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly2 = createList(arr, n)
        sum = Solution().addPolynomial(poly1, poly2)
        ptr = sum
        while ptr is not None:
            print(str(ptr.coef) + 'x^' + str(ptr.power), end = '')
            ptr = ptr.next
            if ptr is not None:
                print(' +', end = ' ')
        print()
            