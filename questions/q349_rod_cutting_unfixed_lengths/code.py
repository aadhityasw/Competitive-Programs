class Solution:
    def cutRod(self, price, n):
        
        table = [0 for _ in range(n+1)]
        
        for i in range(1, n+1) :
            table[i] = price[i-1]
            for j in range(n//2 + 1) :
                table[i] = max(
                    table[i],
                    table[j] + table[i-j]
                )
        
        return table[n]


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
