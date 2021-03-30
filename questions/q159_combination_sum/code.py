class Solution:
    def recursiveCount(self, arr, summ, current) :
        if summ < 0 :
            return
            
        if summ == 0 :
            if current not in self.sets :
                self.sets.append(current)
            return
        
        for i in range(len(arr)) :
            self.recursiveCount(arr[i+1:], summ - arr[i], current + [arr[i]])


    def combinationSum(self, A, N, B):
        
        A.sort()
        self.sets = []

        self.recursiveCount(A, B, [])

        return self.sets


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        B = int(input())
        
        ob = Solution()
        result = ob.combinationSum(A, N, B)
        if(len(result) == 0):
            print("Empty")
        else:
            for i in range(len(result)):
                print("(",end="")
                for j in range(len(result[i])):
                    print(result[i][j],end="")
                    if(j < len(result[i])-1):
                        print(" ",end="")
                print(")",end="")
            print()
