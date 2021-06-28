import heapq

class Solution:

    def getGreatestFromHeap(self, ele, heap) :
        """
        Given a heap and the element to be searched, we return the next largest number smaller than the element from the heap.
        """

        # If the heap is empty return None
        if len(heap) == 0 :
            return -1 * float("inf")
        
        # Traverse till we find the largest element smaller than ele
        val = -1 * float("inf")
        queue = [0]
        while len(queue) > 0 :
            # Extract the next position to cover
            pos = queue.pop(0)
            # If we have hit an invalid position, return
            if pos >= len(heap) or heap[pos] >= ele :
                return val
            # Store the new value if maximum
            val = max(val, heap[pos])
            # Take up the next routes to follow
            if 2*pos+1 < len(heap) and heap[2*pos+1] < ele :
                queue.append(2*pos+1)
            if 2*pos+2 < len(heap) and heap[2*pos+2] < ele :
                queue.append(2*pos+2)
        
        return val



    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # Find the length of this array
        n = len(A)

        # Initialize a variable to store the maximum sum
        max_sum = -1 * float("inf")

        # Initialize a heap to store the right side elements
        heap = []

        # To store the maximum element till that place
        max_arr = [0]*n
        max_arr[n-1] = A[n-1]
        # Fill this array
        for i in range(n-2, -1, -1) :
            max_arr[i] = max(max_arr[i+1], A[i])

        # For every number assume that it is the middle of the triplet
        for i in range(n) :
            
            # Search for the greatest element to the left less thatn A[i]
            ele = self.getGreatestFromHeap(A[i], heap)

            # If we cannot find a predecessor, we continue
            if ele == -1 * float("inf") :
                # Store the current element in the heap
                heapq.heappush(heap, A[i])
                continue

            # If we cannot find a successor, we continue
            if max_arr[i] <= A[i] :
                # Store the current element in the heap
                heapq.heappush(heap, A[i])
                continue

            # If we can form a triplet, then consider it
            max_sum = max(max_sum, (ele + A[i] + max_arr[i]))

            # Store the current element in the heap
            heapq.heappush(heap, A[i])
            
        # Return this maximum sum
        return max_sum


A = [ 31844, 16711, 14509, 26490, 9859, 10185, 18122, 10107, 6587, 23988, 31372, 32491, 24973, 10519, 2074, 32354, 1282, 2663, 27997, 28214, 9452, 29116, 8805, 19786, 20334, 21565, 10505, 12838, 11454, 13785, 16334, 16973, 26922, 31545, 15371, 13258, 89, 6130, 20298, 3341, 19924, 27902, 15344, 5877, 1732, 27501, 15649, 13614, 254, 20312, 9694, 6333, 27452, 1815, 31600, 217, 23213, 6835, 3850, 32253, 20913, 10142, 23210, 27451, 9181, 17570, 9536, 4563, 23366, 25112, 12818, 11012, 764, 31322, 32607, 13346, 31444, 9851, 22594, 18665, 14443, 27445, 15834, 30737, 6503, 21026, 27560, 17954, 11008, 9007, 31544, 21130, 2752, 21071, 27396, 21229, 17542, 30060, 3221, 22716, 20945, 22179, 7659, 5385, 7739, 30384, 4639, 3738, 13636, 5031, 19783, 32316, 32081, 2022, 22426, 17753, 9205, 5447, 19413, 13005, 8046, 28826, 1245, 2550, 26995, 8530, 20133, 10, 22317, 2430, 7762, 9134, 12931, 10747, 5533, 25284, 30874, 30440, 21881, 8836, 24988, 20571, 25590, 7630, 5561, 29522, 10598, 32190, 13164, 30445, 18622, 24706, 2816, 10714, 22335, 17000, 13138, 25616, 14165, 32059, 23512, 8384, 6847, 20944, 32738, 29832, 28656, 12252, 24352, 13291, 16053, 12296, 24421, 24062, 14361, 29768, 15274, 8035, 32134, 25192, 9302, 379, 25388, 27880, 13501, 6616, 12710, 24073, 25062, 19953, 10971, 22824, 18065, 32538, 22051, 1611, 28792, 12979, 22444, 7162, 4822, 2719, 22299, 15184, 16934, 8696, 14710, 21073, 7469, 8704, 12865, 30846, 1850, 9051, 28647, 31143, 22445, 12156, 26460, 769, 8886, 30302, 769, 9848, 32607, 3188, 14536, 10310, 28365, 17634, 19352, 19141, 18626, 31725, 15347, 3201, 20839, 26032, 11222, 3218, 23625, 13585, 14816, 2345, 8353, 12020, 6071, 11368, 8920, 32175, 24488, 7031, 22346, 22717, 28045, 31700, 25163, 21686, 16116, 25322, 6503, 28542, 7805, 25574, 10734, 11453, 7812, 12230, 2225, 22160, 9984, 31666, 3846, 13951, 6827, 8592, 26898, 23214, 22372, 11987, 14663, 15191, 5585, 21907, 5419, 21623, 27720, 29667, 16219, 1992, 30960, 9567, 17104, 23280, 30499, 4868, 21346, 26104, 17431, 30021, 6026, 1535, 5822, 31834, 16236, 10288, 28394, 4828, 3349, 16625, 32693, 11919, 12801, 17245, 6432, 9087, 9696, 11509, 21754, 11598, 23193, 31122, 2820, 8908, 29072, 5023, 20562, 1992, 22053, 5252, 1524, 28966, 24957, 26981, 15062, 28466, 27524, 12301, 25829, 29236, 27954, 24613, 13683, 23877, 6158, 5290, 3293, 15200, 1777, 2462, 20843, 19132, 27661, 8701, 11639, 21081, 24621, 2546, 30930, 30169, 14142, 18763, 20835, 31634, 32271, 23083, 10001, 14561, 1365, 6142, 16100, 6337, 7666, 6834, 29030, 28828, 27255, 21029, 10320, 5985, 27111, 30169, 24418, 29398, 8126, 7407, 11411, 28464, 32049, 4691, 4970, 5345, 28600, 14644, 10156, 12465, 14538, 5559, 17207, 16912, 29415, 19948, 21294, 9130, 26588, 14081, 86, 8765, 7235, 17077, 14016, 30119, 13385, 24848, 20649, 20548, 5556, 10833, 26782, 30838, 27428, 25897, 5860, 8325, 27800, 15654, 7702, 28842, 4405, 15730, 19216, 30566, 3651, 25533, 3084, 29720, 18297, 24440, 779, 12239, 5242, 20804, 6007, 22621, 32671, 7850, 19206, 4525, 25079, 11788, 21985, 12630, 140, 7899, 19974, 22639, 3816, 21003, 24042, 24486, 15064, 22212, 20067, 18828, 9584, 3931, 26566, 12083, 27983, 8832, 28236, 23291, 11813, 3257, 15803, 1449, 6514, 26127, 18498, 27065, 3216 ]
ob = Solution()
print(ob.solve(A))
