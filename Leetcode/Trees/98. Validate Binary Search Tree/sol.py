# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)

        return min(inOrder(root), key = lambda x: abs(target - x)) # Call lambda function and sort based on the absolute value