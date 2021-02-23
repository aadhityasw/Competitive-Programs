class Node :
    def __init__(self, key, data) :
        self.next = None
        self.prev = None
        self.data = data
        self.key = key


def addNodeFront(node, head, tail) :
    """ Given a node and the head pointer of a linked list, adds the node before the linked list head and returns the head of the list """
    if head is None :
        head = node
        tail = node
        return (head, tail)
    head.prev = node
    node.next = head
    head = node
    return (head, tail)


def removeNode(node, head, tail) :
    """ Given a node in the list, its head and tail pointers, we remove the node from the list and return the head and tail pointers of the list """
    if node is head :
        node = None
        return (None, None)
    if node is tail :
        tail = tail.prev
        tail.next = None
        node.prev = None
        return (head, tail)
    node.prev.next = node.next
    node.next.prev = node.prev
    node.next = None
    node.prev = None
    node = None
    return (head, tail)


class LRUCache:
        
    def __init__(self,cap):
        # cap:  capacity of cache
        self.head = None
        self.tail = None
        self.map = {}
        self.cap = cap
        self.num_entries = 0
        
    
    #This method works in O(1)
    def get(self, key):
        node = self.map.get(key, -1)
        if node == -1 :
            return -1
        if node is not self.head :
            (self.head, self.tail) = removeNode(node, self.head, self.tail)
            (self.head, self.tail) = addNodeFront(node, self.head, self.tail)
        return node.data
        
        
    #This method works in O(1)   
    def set(self, key, value):
        node = self.map.get(key, -1)
        if node == -1 :
            # In case of a miss
            if self.num_entries == self.cap :
                # In case the cache is full
                self.map.pop(self.tail.key)
                (self.head, self.tail) = removeNode(self.tail, self.head, self.tail)
                self.num_entries -= 1
            # Creates a new node and inserts it in the cache and the hashmap
            node = Node(key, value)
            (self.head, self.tail) = addNodeFront(node, self.head, self.tail)
            self.map[key] = node
            self.num_entries += 1
        else :
            if node is not self.head :
                (self.head, self.tail) = removeNode(node, self.head, self.tail)
                (self.head, self.tail) = addNodeFront(node, self.head, self.tail)
            node.data = value
