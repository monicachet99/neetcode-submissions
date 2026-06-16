class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        kr = kl = 0

        if root.left:
            kl = self.maxDepth(root.left)

        if root.right:
            kr = self.maxDepth(root.right)

        return 1 + max(kr, kl)