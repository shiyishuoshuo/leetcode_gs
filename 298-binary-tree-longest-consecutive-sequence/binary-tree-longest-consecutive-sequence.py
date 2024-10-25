# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], parentNode: Optional[TreeNode], length:int) -> int:
            if not node:
                return length
            length = length + 1 if parentNode and parentNode.val + 1 == node.val else 1
            max_left = dfs(node.left, node, length)
            max_right = dfs(node.right, node, length)
            max_length = max(max_left, max_right)
            return max(length, max_length)
            
        return dfs(root, None, 0)