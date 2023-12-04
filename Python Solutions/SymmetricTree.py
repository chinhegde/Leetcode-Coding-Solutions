# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        return self.check(root.left,root.right)
    
    def check(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            a = self.check(left.left,right.right)
            b = self.check(left.right, right.left)
            
            return a and b
        