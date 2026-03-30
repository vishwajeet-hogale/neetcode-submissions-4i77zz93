# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postorder(root):
            nonlocal target
            if root is None:
                return None

            root.left = postorder(root.left)
            root.right = postorder(root.right)

            if root.left is None and root.right is None and root.val == target:
                return None 

            return root

        return postorder(root)
        