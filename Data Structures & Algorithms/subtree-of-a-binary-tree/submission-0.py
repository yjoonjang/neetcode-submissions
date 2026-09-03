# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
        def check_isSameTree(node1, node2):
            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            if node1 is None and node2 is None:
                return True
            if node1.val != node2.val:
                return False
            
            lefts = check_isSameTree(node1.left, node2.left)
            rights = check_isSameTree(node1.right, node2.right)

            return lefts and rights
        
        return check_isSameTree(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check_isSubtree(node1, node2):
            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            if self.isSameTree(node1, node2):
                return True

            left_isSubtree = check_isSubtree(node1.left, node2)
            right_isSubtree = check_isSubtree(node1.right, node2)

            return left_isSubtree or right_isSubtree
        
        return check_isSubtree(root, subRoot)
