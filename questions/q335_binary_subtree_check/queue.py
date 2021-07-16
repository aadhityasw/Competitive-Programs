class Solution:
    
    def isEqualTree(self, T, S) :
        if T is None and S is None :
            return True
        
        if T is None or S is None :
            return False
        
        if T.data != S.data :
            return False
        
        queue = [(T, S)]
        while len(queue) > 0 :
            a, b = queue.pop(0)
            
            if (a and not b) or (b and not a) :
                return False
            
            if a and b :
                
                if a.data != b.data :
                    return False
                
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
        
        return True
        
    
    
    def isSubTree(self, T, S):
        
        if T is None and S is None :
            return True
        
        if T is None or S is None :
            return False
        
        queue = [T]
        
        while len(queue) > 0 :
            node = queue.pop(0)
        
            if node.data == S.data :
                val = self.isEqualTree(node, S)
                if val :
                    return True
            
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
        
        return False
