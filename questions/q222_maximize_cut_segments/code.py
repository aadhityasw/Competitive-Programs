class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):

        # Form a table
        table = [0] * (n+1)

        costs = [x, y, z]
        costs.sort()

        # For each cost include its possibilities
        for j in range(1, n+1) :
            for _, c in enumerate(costs) :
                if j % c == 0 :
                    table[j] = max(table[j], (j // c))
                elif j > c and table[j - c] > 0 :
                    table[j] = max(table[j], (table[j - c] + 1))
        
        return table[n]


if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
