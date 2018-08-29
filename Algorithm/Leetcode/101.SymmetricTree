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
     # Solution 1: receusively
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
    # Solution 2: iterative using stack/queue
        def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        stack=[]
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p1,p2=stack.pop(), stack.pop()
            if p1==None and p2==None:
                continue
            if p1==None or p2==None:
                return False
            if p1.val==p2.val:
                stack.append(p1.left)
                stack.append(p2.right)
                stack.append(p1.right)
                stack.append(p2.left)
            else:
                return False
        return True
        
