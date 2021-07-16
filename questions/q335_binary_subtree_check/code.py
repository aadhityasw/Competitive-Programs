class Solution:

    def getPreorder(self, root) :
        if root is None :
            return "N"
        
        s = str(root.data)
        s += " " + self.getPreorder(root.left)
        s += " " + self.getPreorder(root.right)

        return s
    
    def getInorder(self, root) :
        if root is None :
            return "N"
        
        
        s = self.getInorder(root.left)
        s += " " + str(root.data)
        s += " " + self.getInorder(root.right)

        return s



    def isSubTree(self, T, S):

        T_preorder = self.getPreorder(T)
        S_preorder = self.getPreorder(S)
        T_inorder = self.getInorder(T)
        S_inorder = self.getInorder(S)

        val1 = T_preorder.find(S_preorder)
        val2 = T_inorder.find(S_inorder)

        if val1 == -1 or val2 == -1 :
            return False
        return True
