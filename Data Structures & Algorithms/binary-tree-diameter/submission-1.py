# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.res = 0

#         def dfs(root):
#             if not root:
#                 return 0
#             left = dfs(root.left)
#             right = dfs(root.right)
#             self.res = max(self.res, left + right)

#             return 1 + max(left, right)
        
#         dfs(root)
#         return self.res

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxlen = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maxlen = max(self.maxlen, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.maxlen