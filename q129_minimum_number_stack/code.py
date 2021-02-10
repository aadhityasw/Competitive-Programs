class stack:
    def __init__(self):
        self.s=[]
        self.minEle=-1

    def push(self,x):
        if len(self.s) == 0 :
            self.minEle = x
        else :
            if x < self.minEle :
                y = (x * 2) - self.minEle
                self.minEle = x
                x = y
        self.s.append(x)

    def pop(self):
        if len(self.s) == 0 :
            return -1
        else :
            x = self.s.pop(-1)
            if x < self.minEle :
                y = (self.minEle * 2) - x
                x = self.minEle
                self.minEle = y
            
            if len(self.s) == 0 :
                self.minEle = -1
            
            return x

    def getMin(self):
        return self.minEle



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()
