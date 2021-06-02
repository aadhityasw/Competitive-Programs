class Solution:
    def kthElement(self, arr1, arr2, n, m, k):

        # If we are left with one number to choose, we return the minimum of the two arrays
        if k == 1 :
            if n > 0 and m > 0 :
                return min(arr1[0], arr2[0])
            if n > 0 :
                return arr1[0]
            return arr2[0]
        
        if n == 0 :
            return arr2[k-1]
        if m == 0 :
            return arr1[k-1]
        
        # Find the middle point
        mid1 = n // 2
        mid2 = m // 2

        # If the k'th number lies to the right half of the arrays
        if mid1 + mid2 + 2 <= k :
            # If the middle number of arr1 is greater, then we constrict the search to the right portion of the other array and this array remains the same
            if arr1[mid1] > arr2[mid2] :
                return self.kthElement(arr1, arr2[mid2+1:], n, m-mid2-1, k-mid2-1)
            # On the other hand if the middle element of arr2 is greater, then we only constrict the search to right portion of arr1
            else :
                return self.kthElement(arr1[mid1+1:], arr2, n-mid1-1, m, k-mid1-1)
        # If the k'th number lies to the left half of the arrays
        else :
            # If the middle number of arr1 is greater, we constrict the search to left half of this array
            if arr1[mid1] > arr2[mid2] :
                return self.kthElement(arr1[:mid1], arr2, mid1, m, k)
            # If the middle number of arr2 is greater, we constrict the search to left half of this array
            else :
                return self.kthElement(arr1, arr2[:mid2], n, mid2, k)


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()
