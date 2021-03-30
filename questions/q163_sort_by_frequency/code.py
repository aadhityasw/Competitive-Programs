import collections
        
T = int(input())

for _ in range(T) :
    n = int(input())
    arr = list(map(int, input().strip().split()))

    frequency = collections.Counter(arr)
    # Because we sort first by the frequency values in decending order, and then by the actual key value in ascending value(and so the multiplication by -1 for the key)
    keys = sorted(frequency.keys(), reverse=True, key=lambda k : (frequency[k], -1*k))

    i = 0
    for k in keys :
        arr[i:i+frequency[k]] = [k] * frequency[k]
        i += frequency[k]
    
    print(" ".join(list(map(str, arr))))

