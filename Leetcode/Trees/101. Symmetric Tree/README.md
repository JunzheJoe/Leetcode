# 101. Symmetric Tree

🔗 **[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Tree, Depth-First Search (DFS), Breadth-First Search (BFS), Recursion  

---

## Problem Statement

Given the `root` of a binary tree, **check whether it is a mirror of itself** (i.e., symmetric around its center).

---

## Examples

### Example 1:
**Input:**  
```
root = [1,2,2,3,4,4,3]
```
**Output:**  
```python
true
```
**Explanation:**  
- The tree is **symmetric** because the left and right subtrees are mirrors of each other.

### Example 2:
**Input:**  
```
root = [1,2,2,null,3,null,3]
```
**Output:**  
```python
false
```
**Explanation:**  
- The tree is **not symmetric** because the right subtree has a different structure than the left subtree.

---

## Constraints
- `1 <= number of nodes <= 1000`
- `-100 <= Node.val <= 100`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. **What does "symmetric" mean?**  
   - A tree is **symmetric** if its **left subtree is a mirror of its right subtree**.
2. **What traversal method works best?**  
   - **Recursive DFS**: Check if left and right subtrees are **mirrors** at every level.
   - **Iterative BFS**: Use a **queue** to compare nodes level by level.

### 2️⃣ Match
- This is a **Binary Tree + Mirror Property** problem.
- **Recursive DFS** and **Iterative BFS (queue-based)** are both valid approaches.

### 3️⃣ Plan (Recursive Approach)
1. Define a helper function `isSameTree(p, q)`.
2. If both nodes are `None`, return `True`.
3. If one is `None` while the other is not, return `False`.
4. If values of `p` and `q` are different, return `False`.
5. Recursively check:
   - `p.left` with `q.right` (mirroring)
   - `p.right` with `q.left` (mirroring)

---

## 4️⃣ Implementation (Recursive Approach)
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the number of nodes.

- **Time Complexity:** `O(N)`  
  - Each node is visited **once** in DFS.
- **Space Complexity:** `O(H)` (where `H` is the height of the tree)  
  - In the worst case (skewed tree), recursion stack reaches `O(N)`.
  - In a balanced tree, recursion stack is `O(log N)`.

---

## 6️⃣ Additional Notes
- **Recursive DFS** is simple but may cause **stack overflow** for large trees.
- **Iterative BFS Alternative:**  
  - Use a **queue** and compare nodes level-by-level.

---

## 📝 Related Problems
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
