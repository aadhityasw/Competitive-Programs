import collections
import math
import heapq

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):

        a2_dict = dict(collections.Counter(A2))
        a2_ordered = []
        for i in range(M) :
            if A2[i] not in a2_ordered :
                a2_ordered.append(A2[i])

        # Remaining elements are in range 0 <= x <= 10^6
        # So we form an hash table, where each element of the hash table is an heap
        remaining = [[] for _ in range(7)]

        # To store the elements which are also in a2
        a1_dict = {}

        # Store the elements in a hash tables + heap, or in a dictionary of it is in A2
        for ele in A1 :
            if ele in a2_dict :
                if ele in a1_dict :
                    a1_dict[ele] += 1
                else :
                    a1_dict[ele] = 1
            else :
                pos = int(math.log(ele, 10))
                heapq.heappush(remaining[pos], ele)
            
        # Store the elements in the A1 in the order mentioned
        i = 0
        # Insert all the a2 elements which are there in a1
        for a2_ele in a2_ordered :
            if a2_ele in a1_dict :
                A1[i:i+a1_dict[a2_ele]] = [a2_ele] * a1_dict[a2_ele]
                i += a1_dict[a2_ele]
        # add all the remaning elements
        for j in range(7) :
            while len(remaining[j]) > 0 :
                A1[i] = heapq.heappop(remaining[j])
                i += 1
        
        return A1

