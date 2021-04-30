class Solution:
    
    def dijkstra(self, V, adj, S):
        '''
        Function to construct and return cost of MST for a graph represented using adjacency matrix representation
        
        ### Parameters

        * V: nodes in graph
        * adj: adjacency list for the graph
        * S: Source
        '''

        distance = [float("inf")] * V
        distance[S] = 0

        visited = [False] * V
        remaining_count = V

        while remaining_count > 0 :

            # Get an unvisited node with minimum distance measure
            min_value = float("inf")
            for i in range(V) :
                if distance[i] < min_value and not visited[i] :
                    min_node = i
                    min_value = distance[i]
            
            # Visit the min_node
            remaining_count -= 1
            visited[min_node] = True

            # Update the weights
            for (a, weight) in adj[min_node] :
                if distance[a] > distance[min_node] + weight :
                    distance[a] = distance[min_node] + weight
        
        return distance



import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
