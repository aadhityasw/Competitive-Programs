def isSubset( a1, a2, n, m):
    a_set = set(a1)
    b_set = set(a2)
    c_set = set(a1 + a2)
    if len(c_set) in [len(a_set), b_set] :
        return "Yes"
    return "No"


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
