# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        idx = {val: i for i, val in enumerate(inorder)}
        self.pre = 0

        def build(lo, hi):
            if lo > hi:
                return None
            val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(val)
            root_index = idx[val]
            root.left = build(lo, root_index - 1)
            root.right = build(root_index + 1, hi)
        
            return root
        return build(0, len(inorder)-1)
