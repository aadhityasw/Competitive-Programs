class Solution:

    def recursiveDFS(self, i) :

        if self.num_visited == self.N :
            return True

        if self.A[i][-1] in self.string_map :
            for j in self.string_map[self.A[i][-1]] :
                if not self.visited[j] :
                    self.visited[j] = True
                    self.num_visited += 1
                    if self.recursiveDFS(j) :
                        return True
                    self.visited[j] = False
                    self.num_visited -= 1
        
        return False


    def isCircle(self, N, A):

        self.string_map = {}
        for i in range(N) :
            if A[i][0] in self.string_map :
                self.string_map[A[i][0]].append(i)
            else :
                self.string_map[A[i][0]] = [i]
        
        self.visited = [False]*N
        self.num_visited = 0
        self.A = A
        self.N = N

        self.visited[0] = True
        res =  self.recursiveDFS(0)

        if res :
            return 1
        return 0
