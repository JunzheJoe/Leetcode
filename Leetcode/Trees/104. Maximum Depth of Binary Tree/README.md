# 104. Maximum Depth of Binary Tree

🔗 **[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Tree, Depth-First Search (DFS), Breadth-First Search (BFS), Recursion  

---

## Problem Statement

Given the `root` of a binary tree, return its **maximum depth**.

A binary tree's **maximum depth** is the number of **nodes along the longest path** from the root node down to the farthest leaf node.

---

## Examples

### Example 1:
**Input:**  
```
root = [3,9,20,null,null,15,7]
```
**Output:**  
```python
3
```
**Explanation:**  
The longest path is from `3 → 20 → 15` or `3 → 20 → 7`, which has `3` nodes.

### Example 2:
**Input:**  
```
root = [1,null,2]
```
**Output:**  
```python
2
```
**Explanation:**  
The longest path is `1 → 2`, which has `2` nodes.

---

## Constraints
- `0 <= number of nodes <= 10^4`
- `-100 <= Node.val <= 100`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. **What does "maximum depth" mean?**  
   - The number of **nodes** in the longest root-to-leaf path.
2. **What traversal method works best?**  
   - **Recursive DFS**: Simple top-down traversal.
   - **Iterative BFS**: Level-order traversal using a queue.

### 2️⃣ Match
- This is a **Tree Traversal** problem.
- **DFS (Recursion)** and **BFS (Queue-Based)** are valid approaches.

### 3️⃣ Plan (Recursive DFS Approach)
1. **Base Case:** If `root` is `None`, return `0`.
2. Recursively compute **left subtree depth**.
3. Recursively compute **right subtree depth**.
4. The depth of the current node is:
   ```python
   max(left_depth, right_depth) + 1
   ```

---

## 4️⃣ Implementation (Recursive DFS Approach)
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the number of nodes.

- **Time Complexity:** `O(N)`  
  - Each node is visited once.
- **Space Complexity:** `O(H)` (where `H` is the height of the tree)  
  - **Balanced Tree:** `O(log N)`
  - **Skewed Tree:** `O(N)`

---

## 6️⃣ Additional Notes
- **Recursive DFS** is simple but may cause **stack overflow** for deep trees.
- **Iterative BFS Alternative:**  
  - Use a **queue** and track levels.

---

## 📝 Related Problems
- [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
