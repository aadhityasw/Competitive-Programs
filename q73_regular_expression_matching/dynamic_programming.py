class Solution:

    def recursiveDFS(self, s, p, i, j) :
        if i == j == -1 :
            self.buffer[(i, j)] = True
            return
        elif i == -1 :
            if p[j] == '*' :
                self.recursiveDFS(s, p, i, j-2)
                self.buffer[(i, j)] = self.buffer[(i, j-2)]
            else :
                self.buffer[(i, j)] = False
            return
        elif j == -1 :
            self.buffer[(i, j)] = False
            return
        if (i, j) in self.buffer :
            return
        if s[i] == p[j] or p[j] == '.' :
            self.recursiveDFS(s, p, i-1, j-1)
            self.buffer[(i, j)] = self.buffer[(i-1, j-1)]
        elif p[j] == '*' :
            self.recursiveDFS(s, p, i, j-2)
            self.buffer[(i, j)] = self.buffer[(i, j-2)]
            if s[i] == p[j-1] or p[j-1] == '.' :
                self.recursiveDFS(s, p, i-1, j)
                self.buffer[(i, j)] = self.buffer[(i, j)] or self.buffer[(i-1, j)]
        else :
            self.buffer[(i, j)] = False


    def isMatch(self, s: str, p: str) -> bool:
        self.buffer = {}
        self.recursiveDFS(s, p, len(s)-1, len(p)-1)
        return self.buffer[(len(s)-1, len(p)-1)]
