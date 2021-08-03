from collections import defaultdict


class Solution:

    def DFS(self, node, adj, visited) :
        """
        Performs a DFS Search from the vertex given, marking all the visited nodes on the way.

        Parameters
        ----------
        * node - currently visiting node
        * adj - the adjacency list representation of the graph
        * visited - array to keep track of all the nodes already visited during the search procedure
        """

        # Mark the current node as visited
        visited[node-1] = True

        # Visit all its neighboring nodes
        for v in adj[node] :
            if not visited[v-1] :
                self.DFS(v, adj, visited)


    def isConnected(self, V, adj) :
        """
        Given a graph, determines, if all the nodes with edges in the graph are connected or not.

        Parameters
        ----------
        * V - the number of vertices in the graph
        * adj - the adjacency list representation of the graph

        Return
        ------
        * a boolean value denoting if the vertices with edges form a connected component or not
        """

        # If there are no edges
        if not any([len(v) for v in adj.values()]) :
            return True
        
        # Initialize a visited array
        visited = [False]*V

        # Perform a DFS Search with the first vertex with an edge
        self.DFS(list(adj.keys())[0], adj, visited)

        # If any vertex with non-zero edges is not visited, then the component is not connected
        for v in adj.keys() :
            if not visited[v-1] :
                return False
        
        # Return True otherwise
        return True


    def isEularCircuitExist(self, V, adj):

        if not self.isConnected(V, adj) :
            # We cannot form a Euler path or circuit
            return 0

        # We count the number of vertices with odd number of edges
        odd_edges_count = 0
        for v in adj.keys() :
            if len(adj[v]) % 2 == 1 :
                odd_edges_count += 1
        
        if odd_edges_count == 0 :
            # The graph is an Eulerian Circuit
            return 2
        elif odd_edges_count == 2 :
            # The graph is an Eulerian Path
            return 1
        
        # Return if the graph does not satisfy any Eulerian Properties
        return 0




if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = defaultdict(list)
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isEularCircuitExist(V, adj)
        print(ans)
