class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self) :
        self.head = None
        self.tail = None
    
    # Method to add an item to the queue
    def push(self, item): 
        temp = Node(item)
        
        if self.head is None :
            self.head = temp
            self.tail = temp
        else :
            self.tail.next = temp
            self.tail = self.tail.next
         
    
    # Method to remove an item from queue
    def pop(self):
        if self.head is not None :
            ptr = self.head
            self.head = ptr.next
            data = ptr.data
            ptr = None
            return data
        else :
            return -1


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()
