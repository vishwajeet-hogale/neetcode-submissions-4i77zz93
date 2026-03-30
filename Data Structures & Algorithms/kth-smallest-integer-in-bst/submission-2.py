# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = -1
        def inorder(root):
            nonlocal res, k
            if root is None:
                return
            
            inorder(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            inorder(root.right)
            return

        inorder(root)
        return res