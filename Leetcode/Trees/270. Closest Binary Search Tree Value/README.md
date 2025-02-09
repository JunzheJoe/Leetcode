# 270. Closest Binary Search Tree Value

🔗 **[Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Binary Search Tree (BST), Tree Traversal, Inorder Traversal  

---

## Problem Statement

Given the `root` of a **binary search tree (BST)** and a **target** value,  
return the **value in the BST that is closest to the target**.

If there are multiple answers, return the **smallest one**.

---

## Examples

### Example 1:
**Input:**  
```
root = [4,2,5,1,3], target = 3.714286
```
**Output:**  
```python
4
```
**Explanation:**  
- The closest values to `3.714286` in the BST are `3` and `4`.  
- Since `4` is the **smallest** among them, we return `4`.

### Example 2:
**Input:**  
```
root = [1], target = 4.428571
```
**Output:**  
```python
1
```
**Explanation:**  
- The only available value is `1`, so we return `1`.

---

## Constraints
- `1 <= number of nodes <= 10^4`
- `0 <= Node.val <= 10^9`
- `-10^9 <= target <= 10^9`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. **What does "closest value" mean?**  
   - The node value with the **smallest absolute difference** from the target.
2. **What traversal method works best?**  
   - **Inorder traversal (sorted order in BST)** gives easy access to values.
   - **Binary Search (Optimized Approach)** finds the closest efficiently.

### 2️⃣ Match
- This is a **Binary Search Tree (BST) problem**.
- **Inorder Traversal (Recursive DFS)** collects all values first.
- **Binary Search (Iterative DFS)** optimizes space complexity.

### 3️⃣ Plan (Inorder Traversal Approach)
1. Define a **helper function** `inOrder(root)`:
   - If `root` is `None`, return `[]`.
   - Recursively **traverse left subtree**.
   - Add `root.val` to the list.
   - Recursively **traverse right subtree**.
2. After the traversal, find the **minimum difference**:
   ```python
   return min(inOrder(root), key=lambda x: abs(target - x))
   ```

---

## 4️⃣ Implementation (Inorder Traversal Approach)
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the number of nodes.

- **Time Complexity:** `O(N)`  
  - Inorder traversal visits every node once.
- **Space Complexity:** `O(N)`  
  - Stores `N` values in an array.

---

## 6️⃣ Additional Notes
- **Optimized Iterative Approach (O(log N) Time, O(1) Space):**
  - Instead of storing values, **use a pointer to track the closest value**.
  - This reduces **space complexity to O(1)**.

---

## 📝 Related Problems
- [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)
- [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
