def sort012(arr,n):
    num = [0, 0, 0]
    for no in arr :
        num[no] += 1
    
    pos = 0
    for i in range(n) :
        while num[pos] == 0 :
            pos += 1
        arr[i] = pos
        num[pos] -= 1




if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
