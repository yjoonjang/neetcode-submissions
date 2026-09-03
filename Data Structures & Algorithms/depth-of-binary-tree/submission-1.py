# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return 0
        queue = deque([root])
        while queue:
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
        
        