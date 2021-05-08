class Solution:

    def topological_Sort(self, graph, node, visited, stack) :
        visited[node] = True
        for vertex in graph[node] :
            if not visited[vertex] :
                self.topological_Sort(graph, vertex, visited, stack)
        stack.append(node)
    

    def findOrder(self,dict, N, K):
        graph = [set() for _ in range(K)]

        for i in range(N-1) :
            s1 = dict[i]
            s2 = dict[i+1]

            # Form the graph
            pos = 0
            while pos < len(s1) and pos < len(s2) and s1[pos] == s2[pos] :
                pos += 1
            if pos >= len(s1) or pos >= len(s2) :
                continue
            else :
                graph[ord(s1[pos])-97].add(ord(s2[pos])-97)

        # Find a path that covers all the nodes of the graph
        # Topologically sort the graph
        visited = [False]*K
        path = []
        for i in range(K) :
            if not visited[i] :
                self.topological_Sort(graph, i, visited, path)
        path.reverse()
        
        ans = "".join([chr(i+97) for i in path])
        return ans







class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)
        
        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)
