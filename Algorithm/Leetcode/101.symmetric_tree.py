# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ismirror(l,r):
            if l==None and r==None:
                return True
            elif l==None or r==None:
                return False
            elif l.val==r.val:
                return ismirror(l.left,r.right) and ismirror(l.right,r.left)
            else:
                return False
        
        
        return ismirror(root,root)
        
