# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 1
        # output = []
        self.cnt = 0
        
        def dfs(node, max_so_far):   # max_so_far = 여기 오는 길의 최댓값
            if node is None:
                return
            # 1. 지금 노드가 good인지 판단: node.val이 max_so_far보다 크거나 같은가?
            #    good이면 카운트 +1
            if node.val >= max_so_far:
                self.cnt += 1
            # 2. 자식한테 넘겨줄 새 최댓값 계산: max(max_so_far, node.val)
            max_so_far = max(max_so_far, node.val)
            # 3. 그 새 최댓값을 들고 왼쪽·오른쪽으로 내려감
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        
        dfs(root, root.val)
        return self.cnt


