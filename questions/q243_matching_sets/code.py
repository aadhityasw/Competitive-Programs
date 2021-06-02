T = int(input())
for _ in range(T) :
    n = int(input())
    karr = list(map(int, input().strip().split()))

    count = 0
    for i in range(n) :
        for j in range(i+1, n) :
            if (karr[i] | karr[j]) <= max(karr[i], karr[j]) :
                count += 1
    
    print(count)
