# 98. Validate Binary Search Tree

🔗 **[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Binary Search Tree (BST), Recursion, DFS  

---

## Problem Statement

Given the `root` of a binary tree, determine if it is a **valid binary search tree (BST)**.

A **valid BST** is defined as follows:
1. The **left subtree** of a node contains only nodes with keys **less than** the node's key.
2. The **right subtree** of a node contains only nodes with keys **greater than** the node's key.
3. **Both the left and right subtrees must also be binary search trees.**

---

## Examples

### Example 1:
**Input:**  
```
root = [2,1,3]
```
**Output:**  
```python
true
```
**Explanation:**  
- `1 < 2 < 3` → This is a valid BST.

### Example 2:
**Input:**  
```
root = [5,1,4,null,null,3,6]
```
**Output:**  
```python
false
```
**Explanation:**  
- The node `4` is in the right subtree of `5`, but `4 < 5` (invalid BST).
- The correct placement for `4` should be in the left subtree of `5`.

---

## Constraints
- `1 <= number of nodes <= 10^4`
- `-2^31 <= Node.val <= 2^31 - 1`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. **What makes a BST valid?**  
   - The left subtree must have values **less than** the root.
   - The right subtree must have values **greater than** the root.
2. **What traversal method works best?**  
   - **Recursive DFS with valid range tracking**.
   - **Iterative inorder traversal** to check sorted order.

### 2️⃣ Match
- This is a **Binary Search Tree Validation** problem.
- **Recursive DFS (Top-Down Approach)** efficiently validates the BST properties.

### 3️⃣ Plan (Recursive DFS Approach)
1. Start with `root` and the valid range **(-∞, ∞)**.
2. If `root` is `None`, return `True` (base case).
3. If `root.val` is **out of the range**, return `False`.
4. Recursively validate:
   - **Left subtree**: Values must be `< root.val`.
   - **Right subtree**: Values must be `> root.val`.

---

## 4️⃣ Implementation (Recursive DFS Approach)
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the number of nodes.

- **Time Complexity:** `O(N)`  
  - Each node is visited **once**.
- **Space Complexity:** `O(H)` (where `H` is the height of the tree)  
  - **Balanced Tree:** `O(log N)`
  - **Skewed Tree:** `O(N)`

---

## 6️⃣ Additional Notes
- **Iterative Inorder Traversal Alternative:**
  - Inorder traversal of a BST should result in a **sorted list**.
  - If a value is **out of order**, return `False`.

---

## 📝 Related Problems
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
