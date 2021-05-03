"""
@Author : aadhityasw
Uses the concept of Eulerian Circuit. Our case is satisfied if we can find an eulerian graph from the given components of the problem.
A Graph has an Eulerian Circuit if :
    1. All the nodes with non-zero edges belong to a single strongly connected component. -- Kosaraju Algorithm
    2. All the nodes have the same number of in and out edges.
The graph is made by considering all the 26 characters of the english language to be nodes, and the edges constitute between the first and the last character of each provided word.
"""


class Solution:

    def DFS(self, adj, stack, visited) :
        """
        Given a graph, a stack to keep track, and a visited array, perform a DFS and record all the visits to the nodes.
        """
        while len(stack) > 0 :
            node = stack.pop(-1)
            for j in adj[node] :
                if not visited[j] and len(adj[j])>0 :
                    visited[j] = True
                    stack.append(j)
    

    def findGraphTranspose(self, adj) :
        """
        Given a graph representation, reverse the edges and returned the transposed graph.
        """
        radj = [[] for _ in range(26)]
        for i in range(26) :
            for j in adj[i] :
                radj[j].append(i)
        return radj


    def verifyKosaraju(self, adj) :
        """
        Given a graph, verify if there is only one strongly connected component in the graph using the KosaRaju's Algorithm
        """

        # Initialize the visited array
        visited = [False] * 26

        # Find the first node with non-zero edges
        node = None
        for i in range(26) :
            if len(adj[i]) > 0 :
                node = i
                break
        if node is not None :
            visited[node] = True
            stack = [node]
        else :
            return False
        
        # Perform DFS starting with this node
        self.DFS(adj, stack, visited)
        # Check if all the nodes with non zero edges have been visited
        for i in range(26) :
            if len(adj[i]) > 0 and not visited[i] :
                return False
        
        # Re-Initialize the visited for reverse graph traversal
        visited = [False] * 26
        # We re-initialize the stack, we fill it with any node which has non-zero node
        # Because each node has equal number of in and out nodes, the node found earlier can be used here as a starting point too, 
        # because if an edge goes out from there, then that edge comes in here, and because of the property the same number of nodes comes out as well.
        stack = [node]
        visited[node] = True
        # Find the transpose of this graph
        reverse_adj = self.findGraphTranspose(adj)

        # Perform DFS for the reversed graph
        self.DFS(reverse_adj, stack, visited)
        # Check if all the nodes with non zero edges have been visited
        for i in range(26) :
            if len(adj[i]) > 0 and not visited[i] :
                return False
        
        return True


    def isCircle(self, N, A):

        # Form the graph
        graph = [[] for _ in range(26)]
        in_node_count = [0]*26
        out_node_count = [0]*26
        for s in A :
            graph[ord(s[0]) - 97].append(ord(s[-1]) - 97)
            in_node_count[ord(s[-1]) - 97] += 1
            out_node_count[ord(s[0]) - 97] += 1
        
        # Check for condition 2 (All nodes should have equal number of in and out edges)
        for i in range(26) :
            if in_node_count[i] != out_node_count[i] :
                return 0
        
        # Check if all the present nodes are under a single connected component
        if self.verifyKosaraju(graph) :
            return 1
        return 0
