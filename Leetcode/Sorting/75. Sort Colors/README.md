# 75. Sort Colors

🔗 **[Sort Colors](https://leetcode.com/problems/sort-colors/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Two Pointers, Sorting, Dutch National Flag Algorithm  

---

## Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **red, white, and blue**.

We will use the integers:
- `0` to represent **red**,
- `1` to represent **white**, and
- `2` to represent **blue**.

You **must solve this problem without using the library's sort function**.

---

## Examples

### Example 1:
**Input:**  
```python
nums = [2,0,2,1,1,0]
```
**Output:**  
```python
[0,0,1,1,2,2]
```

### Example 2:
**Input:**  
```python
nums = [2,0,1]
```
**Output:**  
```python
[0,1,2]
```

---

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. We need to sort the array **in-place** with three distinct values (`0`, `1`, `2`).
2. We cannot use built-in sorting functions.
3. **Can we do this in one pass?** → Yes, using **Dutch National Flag Algorithm**.

---

### 2️⃣ Match
Possible solutions:
- **Sorting (`O(N log N)`)** → Not optimal.
- **Counting (`O(N)`) + Overwrite (`O(N)`)** → Two passes, but better.
- **Dutch National Flag Algorithm (`O(N)`, One-pass, Constant Space)** → Best solution.

---

### 3️⃣ Plan (Dutch National Flag Algorithm)
1. **Use three pointers**:
   - `l` (left) tracks boundary of `0` (red).
   - `r` (right) tracks boundary of `2` (blue).
   - `i` iterates through the array.
2. **Swap elements based on value:**
   - If `nums[i] == 0`, swap with `nums[l]`, move `l` forward.
   - If `nums[i] == 2`, swap with `nums[r]`, move `r` backward.
   - If `nums[i] == 1`, just continue.
3. **Terminate when `i > r`**.

---

## 4️⃣ Implementation
See `sol.py`.

---

## 5️⃣ Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| Sorting | `O(N log N)` | `O(1)` |
| Counting Sort | `O(N)` | `O(1)` |
| **Dutch National Flag** | `O(N)` | `O(1)` |

---

## 6️⃣ Additional Notes
- The **Dutch National Flag Algorithm** sorts the array **in-place** in **one pass**.
- Uses **constant space (`O(1)`)**.

---

## 📝 Related Problems
- [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
