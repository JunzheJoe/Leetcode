from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # List to store the right-side view
        if not root:  # If the tree is empty, return an empty list
            return res

        q = deque([root])  # Initialize the queue with the root node

        while q:  # Perform BFS until the queue is empty
            rightSide = None  # Variable to keep track of the rightmost node in the current level
            qLen = len(q)  # Number of nodes in the current level

            for i in range(qLen):  # Iterate through all nodes in the current level
                node = q.popleft()  # Pop the leftmost node from the queue
                if node:
                    rightSide = node  # Update the rightmost node for this level
                    q.append(node.left)  # Add the left child to the queue (if exists)
                    q.append(node.right)  # Add the right child to the queue (if exists)

            if rightSide:  # After finishing the level, add the rightmost node's value to the result
                res.append(rightSide.val)

        return res  # Return the list containing the right-side view
