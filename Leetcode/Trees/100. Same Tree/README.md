# 100. Same Tree

🔗 **[Same Tree](https://leetcode.com/problems/same-tree/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Tree, DFS, BFS, Recursion  

---

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are **the same or not**.

Two binary trees are **considered the same** if they are:
1. **Structurally identical**, and
2. **The nodes have the same values**.

---

## Examples

### Example 1:
**Input:**  
```
p = [1,2,3], q = [1,2,3]
```
**Output:**  
```python
true
```
**Explanation:**  
Both trees have the same structure and values.

### Example 2:
**Input:**  
```
p = [1,2], q = [1,null,2]
```
**Output:**  
```python
false
```
**Explanation:**  
The structures are **different**, so they are **not the same**.

### Example 3:
**Input:**  
```
p = [1,2,1], q = [1,1,2]
```
**Output:**  
```python
false
```
**Explanation:**  
The structures are the same, but the **values differ**, so they are **not the same**.

---

## Constraints
- `0 <= number of nodes <= 100`
- `-10^4 <= Node.val <= 10^4`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. **What does "same tree" mean?**  
   - **Both trees must have identical structure and values.**
2. **What traversal method works best?**  
   - **Recursive DFS:** Compare nodes **top-down**.
   - **Iterative BFS:** Use **queues** to compare level by level.

### 2️⃣ Match
- This is a **Binary Tree Comparison** problem.
- **DFS (Recursion)** is simple and effective.

### 3️⃣ Plan (Recursive DFS Approach)
1. If **both nodes are `None`**, return `True`.
2. If **only one is `None`**, return `False`.
3. If values differ, return `False`.
4. Recursively check:
   - Left subtree of `p` with left subtree of `q`.
   - Right subtree of `p` with right subtree of `q`.

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
  - Use a **queue** to compare nodes level by level.

---

## 📝 Related Problems
- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
