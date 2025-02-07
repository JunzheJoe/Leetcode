# 110. Balanced Binary Tree

🔗 **[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Tree, Depth-First Search (DFS), Binary Tree  

---

## Problem Statement

Given a binary tree, determine if it is **height-balanced**.

A binary tree is **height-balanced** if:
- The left and right subtrees of **every node** differ in height by at most `1`.

---

## Examples

### Example 1:
**Input:**  
```
root = [3,9,20,null,null,15,7]
```
**Output:**  
```python
true
```
**Explanation:**  
The tree is balanced because for every node, the height difference between the left and right subtree is at most `1`.

### Example 2:
**Input:**  
```
root = [1,2,2,3,3,null,null,4,4]
```
**Output:**  
```python
false
```
**Explanation:**  
The tree is **not balanced** because the left subtree has a height of `4`, while the right subtree has a height of `2`, which exceeds the allowed difference of `1`.

### Example 3:
**Input:**  
```
root = []
```
**Output:**  
```python
true
```
**Explanation:**  
An empty tree is considered balanced.

---

## Constraints
- `0 <= number of nodes <= 5000`
- `-10^4 <= Node.val <= 10^4`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. What does "balanced" mean?  
   - A tree is **balanced** if the height difference between the left and right subtree of **every node** is **≤ 1**.
2. How do we determine the height?  
   - Height of a node = `max(left subtree height, right subtree height) + 1`
3. What is the base case?  
   - An empty tree (`None`) is balanced.

### 2️⃣ Match
- This is a **Binary Tree + DFS (Depth-First Search)** problem.
- Recursively calculate the height of each subtree and check if the difference is ≤ 1.

### 3️⃣ Plan
1. Define a helper function `getHeight(node)`.
2. Recursively calculate the height of **left** and **right** subtrees.
3. If the difference in height is **greater than 1**, return `-1` (indicating imbalance).
4. If any subtree is already unbalanced (`-1`), propagate the `-1` up.
5. If the tree is balanced, return its actual height.

---

## 4️⃣ Implementation
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the number of nodes.

- **Time Complexity:** `O(N)`  
  - Each node is visited **once** and its height is calculated recursively.
- **Space Complexity:** `O(H)` (where `H` is the height of the tree)  
  - In the worst case (skewed tree), recursion stack goes up to `O(N)`.  
  - In a balanced tree, recursion stack is `O(log N)`.

---

## 6️⃣ Additional Notes
- The approach **recursively checks the height of subtrees**.
- Returning `-1` allows **early termination** when imbalance is detected.

---

## 📝 Related Problems
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
