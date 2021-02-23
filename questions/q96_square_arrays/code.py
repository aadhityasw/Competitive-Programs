n, q = map(int, input().split())

arr = [0]* n

for tes in range(q) :
    query = list(map(int, input().split()))
    
    if query[0] == 1 :
        p = 1
        for i in range(query[1]-1, query[2]) :
            arr[i] += (p * (p+1))
            p += 1
    elif query[0] == 2 :
        print(sum(arr[query[1]-1 : query[2]])%109)
