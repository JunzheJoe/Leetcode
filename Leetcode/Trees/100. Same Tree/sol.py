# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q are both None (empty nodes), then return true. If either of them is not empty,
        # then no way they are the same tree
        if p is None or q is None:
            return p is q

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        