class Solution:

    def __init__(self):
        self.store = {
            0 : 0,
            1 : 1
        }

    def findPosition(self, x, arr) :
        """
        Finds the position where x can be inserted into the array, which is used here to determine the index
        """
        front = 0
        rear = len(arr) - 1
        while front < rear :
            mid = (front + rear + 1) // 2
            if arr[mid] < x :
                rear = mid - 1
            else :
                front = mid
        return front

    
    def findProductOfDivisors(self, num) :
        """
        returns the product of divisiors
        """
        if num in self.store :
            return self.store[num]
        
        prod = 1
        for i in range(1, int(num**0.5)+1) :
            if num % i == 0 :
                prod = (prod * i) % (1e9 + 7)
                if i**2 != num :
                    prod =(prod * num / i) % (1e9 + 7)
        self.store[num] = prod
        return prod
        

    def findProductOfDivisorsArray(self, A) :
        """
        given an array, returns its product of divisors of each element
        """

        pod = []
        for ele in A :
            pod.append(self.findProductOfDivisors(ele))
        
        return pod


    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        # Find the length of A
        n = len(A)

        # Sort the array A
        A.sort()

        # Find the G array
        G = self.findProductOfDivisorsArray(A)
        
        # Find the cumulative frequency of each term of reverse of G
        cumulative = [len(G)]
        for i in range(len(G)-1, 0, -1) :
            cumulative.append(cumulative[-1] + i)
        G.reverse()

        answer = []
        for x in B :
            pos = self.findPosition(x-1, cumulative)
            answer.append(G[pos])
        
        return answer



