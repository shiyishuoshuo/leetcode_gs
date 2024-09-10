# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDepthHelper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            return max(maxDepthHelper(node.left), maxDepthHelper(node.right)) + 1

        return maxDepthHelper(root)
        