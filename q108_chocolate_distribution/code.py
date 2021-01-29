T = int(input())

for tes in range(T) :
    n = int(input())
    arr = list(map(int, input().strip().split()))
    m = int(input())

    arr.sort()

    front = 0
    rear = m-1
    val = arr[rear] - arr[front]
    for rear in range(m, n) :
        front += 1
        val = min(val, (arr[rear] - arr[front]))
    
    print(val)
