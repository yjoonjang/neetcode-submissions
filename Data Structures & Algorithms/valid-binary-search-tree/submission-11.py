# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(node, localmax, localmin):
            if node is None:
                return True
            if not (localmin < node.val < localmax):
                return False

            return dfs(node.left, node.val, localmin) and dfs(node.right, localmax, node.val)

        return dfs(root, float('inf'), float('-inf'))    

        