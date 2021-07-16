class Solution:
    
    def isEqualTree(self, T, S) :
        if T is None and S is None :
            return True
        
        if T is None or S is None :
            return False
        
        if T.data != S.data :
            return False
        
        return self.isEqualTree(T.left, S.left) and self.isEqualTree(T.right, S.right)
    
    
    
    def isSubTree(self, T, S):
        
        if T is None and S is None :
            return True
        
        if T is None or S is None :
            return False
        
        if T.data == S.data :
            val = self.isEqualTree(T, S)
            if val :
                return True
        
        return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)
