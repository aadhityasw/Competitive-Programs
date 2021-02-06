class Node:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
    
    def __init__(self) :
        self.head = None

    # The method push to push element into
    # the stack
    def push(self, data):
        temp = Node(data)
        
        if self.head is None :
            self.head = temp
        else :
            temp.next = self.head
            self.head = temp
        

    # The method pop which return the element
    # poped out of the stack
    def pop(self):
        if self.head is not None :
            ptr = self.head
            self.head = ptr.next
            data = ptr.data
            ptr = None
            return data
        else :
            return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()
