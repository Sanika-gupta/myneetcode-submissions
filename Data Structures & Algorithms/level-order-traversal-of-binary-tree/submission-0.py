# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # intialise q with collections.deque()
        q = collections.deque()
        # initialise with the root node so
        q.append(root)
        # start bfs
        while q:
            # while q isnt empty, get the len - num of values in the queue
            qlen = len(q) 
            # done to ensure we go one level at a time
            level = []
            for i in range(qlen):
                node = q.popleft()
                # fifo
                if node:
                    level.append(node.val)
                    # get the children
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

           
        return res


        