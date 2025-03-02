# 42. Trapping Rain Water

🔗 **[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)**  
💡 **Difficulty:** Hard  
🛠 **Topics:** Two Pointers, Dynamic Programming, Stack  

---

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

## Examples

### Example 1:
**Input:**  
```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```
**Output:**  
```python
6
```
**Explanation:**  
The elevation map `[0,1,0,2,1,0,1,3,2,1,2,1]` can trap `6` units of water in the blue section.

### Example 2:
**Input:**  
```python
height = [4,2,0,3,2,5]
```
**Output:**  
```python
9
```
**Explanation:**  
The elevation map `[4,2,0,3,2,5]` can trap `9` units of water.

---

## Constraints
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
- Given an elevation map, we need to compute how much rainwater it can trap.
- Water can be trapped when a bar is surrounded by two taller bars on both sides.

---

### 2️⃣ Match
- This problem is a **prefix-max/suffix-max** problem.
- **Key Observations:**
  - The water trapped on top of any bar `i` is determined by the **minimum of the tallest bars on the left and right**, minus the height of `i`.

---

### 3️⃣ Plan (Prefix & Suffix Maximums Approach)
1. **Precompute left max (`pre_max`) and right max (`suf_max`)**:
   - `pre_max[i]` stores the tallest bar to the **left** of index `i`.
   - `suf_max[i]` stores the tallest bar to the **right** of index `i`.
2. **Calculate trapped water**:
   - For each index `i`, the trapped water is `min(pre_max[i], suf_max[i]) - height[i]`.

---

## 4️⃣ Implementation (Python Code)
see sol.py
---

### 5️⃣ Review
✅ **Tested Happy Path:**  
- `height = [0,1,0,2,1,0,1,3,2,1,2,1]` → `6`  
✅ **Edge Cases:**  
- `height = [4,2,0,3,2,5]` → `9`  
- `height = [1,1,1,1]` → `0` (Flat terrain, no water trapped)  
- `height = [5,4,3,2,1]` → `0` (Descending heights, no trapped water)  

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - We traverse the array **3 times**: once for `pre_max`, once for `suf_max`, and once for calculating water trapped.
- **Space Complexity:** `O(N)`  
  - We store `pre_max` and `suf_max`, each of size `N`.

**Pros:**
- ✅ **Optimal `O(N)` solution** compared to brute force `O(N^2)`.
- ✅ **Easy to understand with prefix & suffix arrays.**

**Cons:**
- ❌ **Uses extra `O(N)` space for precomputed arrays.**
- **Can we optimize?** Yes! The two-pointer approach can reduce space to `O(1)`.

---

## 📝 Optimized Approach: Two Pointers
Instead of storing `pre_max` and `suf_max`, use **two pointers (`left` and `right`)**:
1. Maintain `left_max` and `right_max` variables.
2. Move the pointer pointing to the **shorter height** inward.
3. Update trapped water dynamically.

⏳ **Time Complexity:** `O(N)`, 💾 **Space Complexity:** `O(1)`

---

## 📝 Related Problems
- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) – Similar Two-Pointer approach.
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) – Uses a stack for area calculation.
