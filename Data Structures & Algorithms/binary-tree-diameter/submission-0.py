# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.res

        # if root is None:
        #     return 0
        # queue = deque([root])
        # diameter = 0
        # while queue:
        #     curr_len = len(queue)
        #     for _ in range(curr_len):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     diameter += 1
        
        # return diameter