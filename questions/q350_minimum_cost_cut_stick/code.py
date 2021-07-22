class Solution:

    def recurse(self, cuts, start, end) :
        
        # If invalid segment, return 0
        if start > end :
            return 0
        
        # If we have already done the computation for this segment, return it
        if (start, end) in self.store :
            return self.store[(start, end)]
        
        # Calculate the length of this current segment
        # This will be the cost of making a cut, irrespective of where the cut is made
        segment_length = cuts[end+1] - cuts[start-1]

        # Find the best segment to cut
        minimum_cut_cost = float("inf")
        for i in range(start, end+1) :
            minimum_cut_cost = min(
                minimum_cut_cost,
                segment_length + self.recurse(cuts, start, i-1) + self.recurse(cuts, i+1, end)
            )
        
        # Save and return this value
        self.store[(start, end)] = minimum_cut_cost
        return minimum_cut_cost


    def minCost(self, n: int, cuts) -> int:

        # Add the boundary values for marking the boundaries of the scale
        cuts.append(0)
        cuts.append(n)
        num_cuts = len(cuts)

        # Sort the list of cuts to organize them better
        cuts.sort()

        # Initialize a store for pruning repeated computations
        self.store = {}

        # Find the minimum cost
        self.recurse(cuts, 1, num_cuts-2)

        # Return the minimum cost
        return self.store[(1, num_cuts-2)]


