# Code Chef MAY19F1
# Lost Guy Radhu

test = int(input())
for tes in range(test) :
    n, q = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    queries = list(map(int, input().strip().split(' ')))
    mini = []
    max_val = -1
    max_que = max(queries)
    for i in range(max_que) :
        if a[i] > max_val :
            max_val = a[i]
        mini.append(max_val)
    for i in queries :
        print(mini[i-1])
