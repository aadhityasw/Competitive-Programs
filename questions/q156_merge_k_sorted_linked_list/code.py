import heapq


class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


def mergeKLists(arr,K) :
    
    heap = []
    for i in range(K) :
        heap.append((arr[i].data, i, arr[i]))
    heapq.heapify(heap)

    head = Node(-1)
    ptr = head

    while len(heap) > 0 :
        (v, i, node) = heapq.heappop(heap)

        ptr.next = node
        node = node.next
        ptr = ptr.next
        ptr.next = None

        if node is not None :
            heapq.heappush(heap, (node.data, i, node))

    ptr = head.next
    head.next = None
    head = ptr

    return head







class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = mergeKLists(heads,n)
        printList(merged_list)
