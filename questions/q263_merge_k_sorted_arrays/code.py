import heapq

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):

        # Initialize a heap to store the smallest elemetns of all the k arrays
        heap = []
        heapq.heapify(heap)
        
        # Fill in the first elements of all the k arrays
        # Each element is (element, array_index, position_in_array)
        for i in range(K) :
            heapq.heappush(heap, (arr[i][0], i, 0))

        # Initialize an array to store the sorted elements
        sorted_elements = []

        # Add the elements into this array until the heap is not empty 
        while len(heap) > 0 :
            
            # Take out the minimum element from the heap
            (min_ele, min_array, min_index) = heapq.heappop(heap)

            # Insert the next element of the min_array of any
            if min_index < K-1 :
                heapq.heappush(heap, (arr[min_array][min_index+1], min_array, min_index+1))
            
            # Insert the minimum element into the sorted array
            sorted_elements.append(min_ele)

        # Return the sorted elements array
        return sorted_elements


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
