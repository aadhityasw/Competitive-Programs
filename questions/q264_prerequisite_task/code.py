
class Solution:

    def hasCycle(self, v, path) :
        """
        Given the path taken until now, and the vertex, checks if there are any cycles
        """

        # If the vertex is already present in the path, then cycle is present
        if path[v] :
            return True

        # Mark the current vertex in the path
        path[v] = True

        # Traverse through all tasks that can be done now
        for neighbor in self.graph[v] :
            # If the neighbor is present in the current path, there is a cycle
            if path[neighbor] :
                return True
            # Keep searching for cycles
            if not self.visited[neighbor] and self.hasCycle(neighbor, path) :
                return True

        # Mark the current vertex as not in path
        path[v] = False
        
        # Mark the current vertex that it has been cleared of no cycles
        self.visited[v] = True

        # Return that there is no cycle
        return False


    def isPossible(self,N,prerequisites):
        
        # Initialize an array to serve as a graph
        # Each element is a list of prerequisites to the task in index i
        self.graph = [[] for _ in range(N)]

        # Fill the graph with the pre-requisites
        for i, j in prerequisites :
            self.graph[j].append(i)
        
        # Perform Cycle detection
        self.visited = [False]*N
        for i in range(N) :
            if not self.visited[i] :
                if self.hasCycle(i, [False]*N) :
                    return False
        
        # If there is no cycle
        return True

    

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
