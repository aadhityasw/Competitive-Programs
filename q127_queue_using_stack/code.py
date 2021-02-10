def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    
    stack1.append(x)


def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    
    while len(stack1) > 0 :
        stack2.append(stack1.pop())
    
    element = -1
    if len(stack2) > 0 :
        element = stack2.pop()
    
    while len(stack2) > 0 :
        stack1.append(stack2.pop())
    
    return element


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
