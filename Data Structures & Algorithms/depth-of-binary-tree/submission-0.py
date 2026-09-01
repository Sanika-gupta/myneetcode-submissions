# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # deepest path is DFS
        if not root:
            return 0
        
        right_d= self.maxDepth(root.right)
        
        left_d= self.maxDepth(root.left)
        return 1+ max(right_d,left_d)