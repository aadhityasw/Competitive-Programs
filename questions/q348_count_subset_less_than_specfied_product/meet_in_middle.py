
"""

                                Not working for all test cases
Fails :

Input:

8
5 6 9 7 7 9 10 4
566

Its Correct output is:

85

And Your Code's output is:

84

"""



class Solution:

    def recurse(self, arr, ind, k, cur_prod, store) :
        
        if cur_prod and cur_prod > k :
            return
        
        for i in range(ind, len(arr)) :
            if cur_prod :
                next_prod = cur_prod * arr[i]
            else :
                next_prod = arr[i]
            
            if next_prod > k :
                return
            
            store.append(next_prod)
            self.recurse(arr, i+1, k, next_prod, store)


    def findProducts(self, arr, k) :

        store = []
        self.recurse(arr, 0, k, None, store)
        return store
    

    def findPosition(self, num, arr) :
        
        if num < arr[0] :
            return 0
        if num > arr[-1] :
            return len(arr)

        front = 0
        rear = len(arr)-1
        
        while front < rear :
            mid = (front + rear + 1) // 2
            if arr[mid] <= num :
                front = mid 
            else :
                rear = mid - 1
        
        # Return the count
        return front + 1


    def numOfSubsets(self, arr, N, K):

        products1 = self.findProducts(arr[:(N//2)], K)
        products2 = self.findProducts(arr[(N//2):], K)
        products2.sort()
        #print(products1, products2)

        total_count = 0
        for num in products1 :
            #val = self.findPosition(K/num, products2)
            #print(num, val)
            total_count += self.findPosition(K/num, products2)
        
        return total_count + len(products1) + len(products2)
