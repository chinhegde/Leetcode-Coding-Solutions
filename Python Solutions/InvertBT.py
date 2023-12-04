# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: return root

        def helper(node):
            print("this is", node.val)
            
            if node.right: helper(node.right)
            if node.left: helper(node.left)
            
            temp = node.right
            node.right = node.left
            node.left = temp
            return node

        return helper(root)

