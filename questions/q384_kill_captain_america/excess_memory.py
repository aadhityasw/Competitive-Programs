"""
                    Causes Memory Error
"""


class Solution:

    def formReversedGraph(self, edges) :
        """
        Given a list of edges, converts it into a adjacency list representation of a graph.

        Parameters
        ----------
        * edges - list of all edges

        Return
        ------
        * graph - a adjacency list representation of the reversed graph
        """

        # Initialize a dictionary for the graph
        graph = {}

        # Add the edges to the graph
        for v, u in edges :
            if u in graph :
                graph[u].add(v)
            else :
                graph[u] = {v}
            if v not in graph :
                graph[v] = set()
        
        # Return the graph
        return graph
    

    def DFS(self, node, reversed_graph, visited) :
        """
        Performs a DFS search in the provided graph
        Parameters
        ----------
        * node - the current node
        * reversed_graph - adjacency list representation of the reversed graph
        * visited - keeps track of all the nodes visited in the current path
        """

        # Mark the current node as visited
        visited[node-1] = True

        # Initialize a set to store all the vertices that can be reached
        setu = {node}

        # Visit all its neighboring nodes
        for v in reversed_graph[node] :
            if v in self.store :
                # If we have completed the preprocessing for the node `v`
                setu = setu.union(self.store[v])
            elif visited[v-1] :
                # If v is in our current path (because of cycle)
                setu.add(v)

                # Mark this node as incomplete
                if v in self.incomplete :
                    self.incomplete[v].add(node)
                else :
                    self.incomplete[v] = {node}
            else :
                setu = setu.union(self.DFS(v, reversed_graph, visited))
        
        # Save the set of nodes that can be visited
        self.store[node] = setu
        
        # If any incomplete are present because of this node, then fill them
        if node in self.incomplete :
            for v in self.incomplete[node] :
                self.store[v] = self.store[v].union(self.store[node])
            del self.incomplete[node]

        # If this value is equal to total number of nodes, then add 1 to the overall count
        if len(setu) == self.n :
            self.count += 1
        
        # Mark the current node as not visited, as we are backtracking
        visited[node-1] = False
        
        # Return the set of nodes that can be visited
        return setu


    def captainAmerica (self, n, num_edges, edges):

        self.n = n
        self.incomplete = dict()

        # Form Reversed graph
        reversed_graph = self.formReversedGraph(edges)

        # Initialize variable to store the number of candidates for captain
        self.count = 0

        # Initialize a store to save all the nodes that can be visited from a vertex
        self.store = {}
        
        # Initialize a visited array for the Search procedure
        visited = [False]*n

        # Start a DFS Search from all nodes
        for i in range(1, n+1) :

            self.DFS(i, reversed_graph, visited)

        # Return the count of rooms to hide
        return self.count
