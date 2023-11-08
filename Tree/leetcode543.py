# 543. Diameter of Binary Tree
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def max_depth(root):
            if not root:
                return -1

            left = max_depth(root.left)
            right = max_depth(root.right)
            res[0] = max(left + right + 2, res[0])

            return 1 + max(left, right)

        max_depth(root)
        return res[0]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution().diameterOfBinaryTree(root=root)
    print(solution)

