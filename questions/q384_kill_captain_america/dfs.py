"""
            Causes TLE Error
"""



class Solution:

    def formGraph(self, edges) :
        """
        Given a list of edges, converts it into a adjacency list representation of a graph.

        Parameters
        ----------
        * edges - list of all edges

        Return
        ------
        * graph - a adjacency list representation of the graph
        """

        # Initialize a dictionary for the graph
        graph = {}

        # Add the edges to the graph
        for u, v in edges :
            if u in graph :
                graph[u].add(v)
            else :
                graph[u] = {v}
            if v not in graph :
                graph[v] = set()
        
        # Return the graph
        return graph
    

    def DFS(self, node, graph, visited) :
        """
        Performs a DFS search in the provided graph
        Parameters
        ----------
        * node - the current node
        * graph - adjacency list representation of the graph
        * visited - keeps track of all the nodes visited in the current path
        """

        # Mark the current node as visited
        visited[node-1] = True
        self.numVisits[node-1] += 1

        # Visit all its neighboring nodes
        for v in graph[node] :
            if not visited[v-1] :
                self.DFS(v, graph, visited)


    def captainAmerica (self, n, num_edges, edges):

        # Form the graph
        graph = self.formGraph(edges)

        # Initialize array to store the number of times a node is visited
        self.numVisits = [0]*n

        # Start a DFS Search from all nodes
        for i in range(1, n+1) :
            # Initialize a visited array for the Search procedure
            visited = [False]*n

            self.DFS(i, graph, visited)
        
        # Find all the nodes which have n visits during the DFS
        count = self.numVisits.count(n)

        # Return the count of rooms to hide
        return count
