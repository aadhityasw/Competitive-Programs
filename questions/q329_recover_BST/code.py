# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findWrongVal(self, root, reach) :
        """
        Given a root and its actual reach, find the node which does not satisfy this condition.
        """

        if root is None :
            return None

        mi, ma = reach
        if root.val <= mi or root.val >= ma :
            return root.val
        
        left = self.findWrongVal(root.left, (mi, root.val))
        if left is not None :
            return left
        
        right = self.findWrongVal(root.right, (root.val, ma))
        if right is not None :
            return right
        
        return None


    def findOther(self, root, val) :
        """
        Given the root and a value, finds its appropriate place in the tree
        """

        if root.val < val :
            if root.right :
                if root.right.val > val :
                    if root.right.left :
                        return self.findOther(root.right, val)
                    else :
                        return root.right.val
                else :
                    return self.findOther(root.right, val)
        
        if root.val > val :
            if root.left :
                if root.left.val < val :
                    if root.left.right :
                        return self.findOther(root.left, val)
                    else :
                        return root.left.val
                else :
                    return self.findOther(root.left, val)
        
        return root.val


	# @param A : root node of tree
	# @return a list of integers
    def recoverTree(self, A):

        wrong_val = self.findWrongVal(A, (float("-inf"), float("inf")))
        second_wrong_val = self.findOther(A, wrong_val)

        ans = [wrong_val, second_wrong_val]
        return ans
