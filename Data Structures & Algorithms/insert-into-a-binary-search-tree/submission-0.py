
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val = val)
        ptr = root
        def insert(root, par):
            nonlocal newNode
            if root is None:
                if val < par.val:
                    par.left = newNode
                else:
                    par.right = newNode
                return

            if newNode.val > root.val:
                insert(root.right, root)
            else:
                insert(root.left, root)
            
            
        if root is None:
            return newNode
        insert(root, None)
        return ptr

        