def rearrange(arr, n): 
    max_ele = arr[n-1] + 1
    min_pos = 0
    max_pos = n-1
    
    for i in range(n) :
        if i%2 == 0 :
            # Position for maximum element
            arr[i] += (arr[max_pos] % max_ele) * max_ele
            max_pos -= 1
        else :
            # Position for the minimum number
            arr[i] += (arr[min_pos] % max_ele) * max_ele
            min_pos += 1
    
    for i in range(n) :
        arr[i] = arr[i] // max_ele


import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
