# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if node is None:
                return None
            if node == p or node == q:   # 내가 찾는 노드 본인이면
                return node              # 나를 올려보냄

            left = dfs(node.left)        # 왼쪽 밑에 뭐 있나
            right = dfs(node.right)      # 오른쪽 밑에 뭐 있나

            # 이제 left, right 결과를 보고 판단:
            #  - 둘 다 값이 있으면 → ???
            if left and right:
                return node
            #  - 한쪽만 있으면 → ???
            if left and not right:
                # left = dfs(node.left.left)
                return left
            if right and not left:
                # right = dfs(node)
                return right
            #  - 둘 다 None이면 → ???
            if not right and not left:
                return None
            # 여기를 네가 채워봐

        return dfs(root)