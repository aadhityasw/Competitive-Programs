T = int(input())
for tes in range(T) :
    n = int(input())
    h = list(map(int, input().split()))
    iq = list(map(int, input().split()))

    arr = [i for i in range(n)]
    rem = []
    cur_h = None
    cur_iq = None
    max_count = 0
    count = 0

    while len(arr) > max_count :
        cur_h = h[arr[0]]
        cur_iq = iq[arr[0]]
        i = 1
        count = 1

        while i < len(arr) :
            while (i < len(arr)) not ((h[arr[i]] > cur_h) and (iq[arr[i]] > cur_iq)) :
                i += 1
            
            if i >= len(arr) :
                break
            
            cur_h = h[arr[i]]
            cur_iq = iq[arr[i]]
            count += 1
            arr.pop(i)
        
        max_count = max(count, max_count)
    
    print(max_count)
        

