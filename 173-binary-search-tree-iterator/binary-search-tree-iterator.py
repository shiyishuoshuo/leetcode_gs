# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self.root = root
        self.pushToLeft(root)
        

    def next(self) -> int:
        cur_node = self.stk.pop()
        self.pushToLeft(cur_node.right)
        return cur_node.val

    
    def pushToLeft(self, node: Optional[TreeNode]) -> None:
        if not node:
            return 
        while node:
            self.stk.append(node)
            node = node.left
       

    def hasNext(self) -> bool:
        return len(self.stk) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()