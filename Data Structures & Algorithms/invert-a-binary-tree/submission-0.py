# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # need to do DFS
        # recursive
        if not root:
            return None
        # use a temp
        temp = root.left
        root.left = root.right
        root.right = temp
        # invert the sub tree
        # invert left tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root