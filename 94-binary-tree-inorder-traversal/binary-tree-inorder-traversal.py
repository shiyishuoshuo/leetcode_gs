# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorderHelper(node: Optional[TreeNode], res:List[int]):
            if not node:
                return res
            inorderHelper(node.left, res)
            res.append(node.val)
            inorderHelper(node.right, res)

        ans = []
        inorderHelper(root, ans)
        return ans
        