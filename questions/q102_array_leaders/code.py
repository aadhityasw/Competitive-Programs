def leaders(A,N):
    lead = []
    ma = A[-1]
    for num in reversed(A) :
        if num >= ma :
            ma = num
            lead.append(ma)
    return reversed(lead)

    # The below code will result in the same answer but will take a lot more time in the process because
    # the addition of two lists take more time than append operation with reverse.
    """        lead = [ma] + lead
    return lead"""


import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        
        A=leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
