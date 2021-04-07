import math


def isSubset( a1, a2, n, m):
    table = [[] for _ in range(6)]
    
    for i in a1 :
        pos = int(math.log(i, 10))
        table[pos].append(i)
    
    for i in a2 :
        pos = int(math.log(i, 10))
        if i not in table[pos] :
            return "No"
    
    return "Yes"


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()
