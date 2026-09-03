# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            if node1 is None and node2 is None:
                return True
            if node1.val != node2.val:
                return False
            # if node1.left is None and node1.right is None and node2.left is None and node2.right is None:
            #     if node1.val == node2.val:
            #         return True
            #     return False
            
            lefts = check(node1.left, node2.left)
            rights = check(node1.right, node2.right)

            return lefts and rights
        
        return check(p, q)