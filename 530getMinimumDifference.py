# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res, prev = float('inf'), float('-inf')

        def dfs(root):
            nonlocal res, prev  #nonlocal�����ı������ⲿǶ�׺����ڵı���
            if not root:
                return
            dfs(root.left)
            res = min(res, root.val - prev)
            prev = root.val
            dfs(root.right)

        dfs(root)
        return res
