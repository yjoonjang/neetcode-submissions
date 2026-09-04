# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if root is None:
        #     return True
        # self.isValid = False

        # def dfs(node):
        #     if node is None:
        #         return None
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if left and left.val < node.val:
        #         self.isValid = True
        #         return node
        #     if left and left.val >= node.val:
        #         self.isValid = False
        #         return
        #     if right and right.val > node.val:
        #         self.isValid = True
        #         return node
        #     if right and right.val <= node.val:
        #         self.isValid = False
        #         return
        #     if not left and not right:
        #         return node
        #     # return None
        
        # dfs(root)
        # return self.isValid

        if root is None:
            return False
        queue = deque([(root, float('inf'), float('-inf'))])

        while queue:
            length = len(queue)

            for _ in range(length):
                node, high, low = queue.popleft()
                if not (low < node.val and node.val < high):
                    return False

                left = node.left
                right = node.right

                if left:
                    queue.append((left, node.val, low))
                if right:
                    queue.append((right, high, node.val))
        
        return True

            

        