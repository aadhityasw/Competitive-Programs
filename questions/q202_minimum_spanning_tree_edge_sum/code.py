import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):

        # Insert all the edges into the heap
        heap = []
        for i in range(V) :
            for j in range(len(adj[i])) :
                heapq.heappush(heap, (adj[i][j][1], i, adj[i][j][0]))

        visited = [False]*V
        num_visited = 0
        summ = 0
        components = {} # component_no : [vertices]
        vertex_comp = {} # vertex : component_no
        num_components = 0
        component_id = 0
        #print(heap)

        while ((num_visited < V) or (num_components > 1 and num_visited == V)) and len(heap) > 0 :
            edge_weight, edge_i, edge_j = heapq.heappop(heap)
            # If both vertices have been visited
            if visited[edge_i] and visited[edge_j] :
                # If both the visited vertices do not belong to same component
                if vertex_comp[edge_i] != vertex_comp[edge_j] :
                    delete_key = vertex_comp[edge_j]
                    for ver in components[vertex_comp[edge_j]] :
                        components[vertex_comp[edge_i]].append(ver)
                        vertex_comp[ver] = vertex_comp[edge_i]
                    num_components -= 1
                    del components[delete_key]
                else :
                    # If both the visited vertices belong to same component
                    continue
            # If both the vertices have not been visited, We create a new component
            elif visited[edge_i] == False and visited[edge_j] == False :
                num_components += 1
                components[component_id] = [edge_i, edge_j]
                vertex_comp[edge_i] = component_id
                vertex_comp[edge_j] = component_id
                component_id += 1
                visited[edge_i] = True
                visited[edge_j] = True
            elif visited[edge_i] == False :
                num_visited += 1
                visited[edge_i] = True
                components[vertex_comp[edge_j]].append(edge_i)
                vertex_comp[edge_i] = vertex_comp[edge_j]
            elif visited[edge_j] == False :
                num_visited += 1
                visited[edge_j] = True
                components[vertex_comp[edge_i]].append(edge_j)
                vertex_comp[edge_j] = vertex_comp[edge_i]
            summ += edge_weight
            
            """print(edge_weight, edge_i, edge_j)
            print(visited)
            print(components)
            print(vertex_comp)"""
        
        return summ



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
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
