# 11. Container With Most Water

🔗 **[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Two Pointers, Greedy  

---

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.  

Find two lines that together with the x-axis form a container, such that the container contains the **most water**.  

Return the **maximum amount of water a container can store**.

**Note:** You may not slant the container.

---

## Examples

### Example 1:
**Input:**  
```python
height = [1,8,6,2,5,4,8,3,7]
```
**Output:**  
```python
49
```
**Explanation:**  
- The best container is formed by the vertical lines at **index 1 and index 8** (height `8` and `7`).
- The width between them is `8 - 1 = 7`, and the height is determined by the **shorter** of the two (`min(8,7) = 7`).
- The **max area** is `7 * 7 = 49`.

### Example 2:
**Input:**  
```python
height = [1,1]
```
**Output:**  
```python
1
```
**Explanation:**  
- The only possible container is between index `0` and index `1`, holding `1 * 1 = 1` unit of water.

---

## Constraints
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
- We need to find the **maximum area** between two vertical lines.
- The **width** is the distance between two indices.
- The **height** is determined by the **shorter** of the two selected lines (bucket effect).
- The best solution uses **Two Pointers** instead of brute force.

---

### 2️⃣ Match
- **Problem Type:** Two Pointers + Greedy
- **Key Observations (Bucket Effect)**:
  - The **area is limited by the shorter line**.
  - Moving the **shorter line might increase the max area**, while moving the taller one **never helps**.

---

### 3️⃣ Plan (Two Pointers Approach)
1. **Initialize two pointers**:
   - `left` at the beginning (`0`).
   - `right` at the end (`n-1`).
2. **Calculate the area** using:
   - `width = right - left`
   - `height = min(height[left], height[right])`
   - `area = width * height`
3. **Move the pointer with the shorter height**:
   - This is based on the **bucket effect**: the shorter one determines the capacity.
   - If `height[left] < height[right]`, move `left += 1` to potentially find a taller left.
   - Else, move `right -= 1`.
4. **Continue until left and right meet**.

---

## 4️⃣ Implementation (Python Code)
see sol.py

---

### 5️⃣ Review
✅ **Tested Happy Path:**  
- `height = [1,8,6,2,5,4,8,3,7]` → `49`  
✅ **Edge Cases:**  
- `height = [1,1]` → `1` (Minimal case)  
- `height = [10000, 1, 10000]` → `10000` (Handles tall edges with a small value in between)  
✅ **Walked through iterations step-by-step.**

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - Each element is checked **once**, and we only **move one pointer per step**.
- **Space Complexity:** `O(1)`  
  - No extra space is used.

**Pros:**
- ✅ **Optimized with Two Pointers.**
- ✅ **Linear time complexity `O(N)`.**
- ✅ **Greedy approach ensures we only move the pointer that helps maximize the area.**

**Cons:**
- ❌ **Does not return which indices form the best container** (only the max water amount).

---

## 📝 Why Move the **Shorter Line**?
This follows the **bucket effect**:
- The **shorter line** is the limiting factor.
- If we move the taller line, the height is still determined by the shorter one.
- Moving the **shorter line** gives a chance to find a **taller line**, potentially increasing the area.

---

## 📝 Related Problems
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) – More complex water storage problem.
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) – Another **Two Pointers** problem.
