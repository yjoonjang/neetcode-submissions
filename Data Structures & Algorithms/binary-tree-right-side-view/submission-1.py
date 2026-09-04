# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        output = []
        queue = deque([root])

        while queue:
            self.val = 0
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.val > self.val:
                    self.val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            output.append(self.val)
        return output