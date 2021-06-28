class Solution:

    def getPower(self, pos, B) :
        """
        Given the position of the light and its general power, we determine its extent of lighting capacity
        """

        # Calcuate its extent
        extent = (
            pos-B+1,
            pos+B-1
        )

        # Return this value
        return extent


    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # Find the length of the corridor
        n = len(A)

        # Initialize a position variable to indicate that all units to its left are successfully lit
        frontier = -1
        pos = 0

        # Initialize a counter to choose the number of lights choosen by us
        count_lights = 0

        # Iterate till we can light all the units of the corridor
        while frontier < n-1 :

            # Figure out the farthest light source that can light (pos+1) position
            candidate = None
            for i in range(pos, n) :
                # If it has a light source, then get its extent
                if A[i] == 1 :
                    extent = self.getPower(i, B)
                    # If this extent can reach pos+1, then it is a candidate
                    if extent[0] <= frontier+1 :
                        # If we dont yet have a candidate, or if this extent goes furrther right than the candidate, then this is our new candidate
                        if candidate is None or candidate[1] < extent[1] :
                            candidate = extent
                            pos = i
                
            # If we do not have a candidate, then there is no chance of lighting this corridor
            if candidate is None :
                return -1

            # Otherwise, we update the position
            frontier = candidate[1]

            # Update the lights count
            count_lights += 1
    
        # Return the total count of lights used
        return count_lights



ob = Solution()
A = [ 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0 ]
B = 12
print(ob.solve(A, B))
