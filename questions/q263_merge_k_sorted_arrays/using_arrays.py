class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        
        # Initialize the pointers for each array
        pointers = [0] * K

        # Initialize an array to store the sorted elements
        sorted_elements = []

        # Add the elements into this array till it is complete with k^2 elements
        while len(sorted_elements) < (K*K) :
            
            # Create an array of all the elements to compare
            comparing_elements = [(arr[i][pointers[i]], i) for i in range(K) if pointers[i] < K]

            # Find the minimum element and the array it belongs to from these elements
            (min_ele, min_arr) = min(comparing_elements)

            # Increment the pointer of the array with the minimum element
            pointers[min_arr] += 1

            # Store this minimum element
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
