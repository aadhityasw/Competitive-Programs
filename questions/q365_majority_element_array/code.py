


class Solution:

    def findCandidate(self, arr) :
        can_index = 0
        count = 1

        for i in range(len(arr)) :
            if arr[can_index] == arr[i] :
                count += 1
            else :
                count -= 1
            
            if count == 0 :
                can_index = i
                count = 1
        
        return can_index


    def isMajority(self, arr, candidate) :
        count = 0
        n = len(arr)
        for i in range(n) :
            if arr[i] == candidate :
                count += 1
            if count > n / 2 :
                return True
        
        return False


    def majorityElement(self, A, N):

        candidate = A[self.findCandidate(A)]
        if self.isMajority(A, candidate) :
            return candidate
        return -1








import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
