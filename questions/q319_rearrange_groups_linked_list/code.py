# You are using Python

class Node() :
    def __init__(self, value=None) :
        self.data = value
        self.next = None


class LinkedList() :
    
    def __init__(self) :
        self.head = None
        self.tail = None
        
    def insertElements(self, arr) :
        """
        Recieves an array of integers and inserts them sequentially into the linked list.
        """
        
        # Loop through each element and insert it into the end of the list
        for num in arr :
            temp_node = Node(num)
            
            # If the linked list is empty, the current number becomes the head of the list
            if self.head is None :
                self.head = temp_node
                self.tail = temp_node
            else :
                # Otherwise, we append the numebr to the end of the list
                self.tail.next = temp_node
                self.tail = temp_node
        
        # Returns the head pointer to the list
        return self.head
    
    
    
def printList(head) :
    """
    When invoked, it prints the linked list in a single line.
    """
    
    # Iterate through the list, printing all values
    ptr = head
    while ptr :
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


def reverseList(head, k) :
    """
    Provided with the head of a linked list, performs the k element reverse, and returns the new head of the modified list
    """

    ptr = head
    new_head = None
    new_tail = None
    
    num_reverse = (n % k) if (n%k) != 0 else k
    while ptr :
        
        left_portion_start = ptr
        
        i = 1
        while ptr.next and i < num_reverse :
            ptr = ptr.next
            i += 1
        
        right_portion_start = ptr.next
        ptr.next = None
        
        if new_head is None :
            new_head = left_portion_start
            new_tail = ptr
        else :
            ptr.next = new_head
            new_head = left_portion_start
        
        ptr = right_portion_start
        num_reverse = k
        
    return new_head
    

# Recieve the values of n, k, and the array of numbers
input_array = list(map(int, input().strip().split()))
n, k, arr = input_array[0], input_array[1], input_array[2:]

linkedlist = LinkedList()
head = linkedlist.insertElements(arr)

new_head = reverseList(head, k)
printList(new_head)




