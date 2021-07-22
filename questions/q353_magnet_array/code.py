class Solution:

    def calculateForce(self, pos, magnets) :

        # Use the given force formula for this computation
        force = 0
        for p in magnets :
            force += (1 / (pos - p))
        
        return force


    def recurse(self, magnets, l, r) :

        pos = (l + r) / 2

        cur_force = self.calculateForce(pos, magnets)

        if abs(cur_force) < 1e-12 :
            return pos
        elif cur_force < 0 :
            # Right side force is more
            return self.recurse(magnets, l, pos)
        else :
            # Left side force is more
            return self.recurse(magnets, pos, r)


    def nullPoints(self, n, magnets, getAnswer):
        
        for i in range(1, n) :
            getAnswer[i-1] = self.recurse(magnets, magnets[i-1], magnets[i])





      
def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob=Solution()
        ob.nullPoints(n, a, getAnswer)
        
        for i in range(0,n-1):
            print("%.2f"%round(getAnswer[i],2), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
