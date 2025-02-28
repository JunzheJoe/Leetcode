# 167. Two Sum II - Input Array Is Sorted

🔗 **[Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Two Pointers, Binary Search, Array  

---

## Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target`.

Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the **indices** of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length `2`.

**Constraints:**
- The tests are generated such that there is **exactly one solution**.
- You may **not** use the same element twice.
- You must use **only constant extra space**.

---

## Examples

### Example 1:
**Input:**  
```python
numbers = [2,7,11,15], target = 9
```
**Output:**  
```python
[1,2]
```
**Explanation:**  
The sum of `2` and `7` is `9`. Therefore, `index1 = 1`, `index2 = 2`.

### Example 2:
**Input:**  
```python
numbers = [2,3,4], target = 6
```
**Output:**  
```python
[1,3]
```
**Explanation:**  
The sum of `2` and `4` is `6`. Therefore, `index1 = 1`, `index2 = 3`.

### Example 3:
**Input:**  
```python
numbers = [-1,0], target = -1
```
**Output:**  
```python
[1,2]
```
**Explanation:**  
The sum of `-1` and `0` is `-1`. Therefore, `index1 = 1`, `index2 = 2`.

---

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is **sorted** in **non-decreasing** order.
- `-1000 <= target <= 1000`
- **Exactly one solution exists.**

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- We are given a sorted array and must **find two numbers that sum up to `target`**.
- The array is **1-indexed**, so we need to return indices **starting from 1**.
- We must use **constant extra space** (`O(1)`).
- **Happy Path Test:**  
  Input: `[2,7,11,15]`, `target=9` → Output: `[1,2]`
- **Edge Cases:**  
  - Smallest input (`numbers` of size `2`).
  - Negative numbers.
  - Large numbers near the constraints.

---

### 2️⃣ Match
- **Problem Category:** Two Pointers, Binary Search.
- **Pattern:**  
  - **Two Pointers Technique**: Since the array is sorted, we can use **two pointers** (`left` and `right`).
  - **Binary Search (Alternative)**: We can use binary search for the second number.

---

### 3️⃣ Plan (Two Pointers)
1. **Initialize two pointers:**
   - `left = 0` (first element).
   - `right = len(numbers) - 1` (last element).
2. **While `left < right`:**
   - Compute `s = numbers[left] + numbers[right]`.
   - If `s == target`, return `[left+1, right+1]`.
   - If `s > target`, move `right` leftward (`right -= 1`).
   - Otherwise, move `left` rightward (`left += 1`).
3. **Return the result once found.**  
   (We are guaranteed exactly one solution.)

---

### 4️⃣ Implement
see sol.py
---

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `[2,7,11,15], target=9` → Output: `[1,2]`
- ✅ **Test with Edge Cases:**  
  - Input: `[2,3,4], target=6` → Output: `[1,3]`  
  - Input: `[-1,0], target=-1` → Output: `[1,2]`
- ✅ **Checked for Logic Bugs:** Two-pointer movement is correctly implemented.
- ✅ **Walked through each iteration step-by-step.**

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - The two pointers traverse the array **at most once**.
- **Space Complexity:** `O(1)`  
  - Uses only two integer variables (`left` and `right`).

**Pros:**  
- Fast and efficient for large inputs.
- No extra space needed.
- Two-pointer technique is **optimal** for sorted arrays.

**Cons:**  
- Only works if the array is **sorted**.
- Requires exactly **one solution** to be guaranteed.

---

### 🔍 Why Two-Pointer Technique Works:
- **Key Insight:**  
  - The array is **sorted**, so we can take advantage of this structure.
  - **If `s > target`**, reducing `right` decreases the sum.
  - **If `s < target`**, increasing `left` increases the sum.
  - This guarantees that we will find the solution in **linear time**.

**Example Walkthrough:**  
```python
numbers = [2, 7, 11, 15], target = 9

Step 1: left = 0, right = 3 → numbers[0] + numbers[3] = 2 + 15 = 17 (too large)
Step 2: right = 2 → numbers[0] + numbers[2] = 2 + 11 = 13 (too large)
Step 3: right = 1 → numbers[0] + numbers[1] = 2 + 7 = 9 (found solution!)
```

---

## 📝 Related Problems
- [1. Two Sum](https://leetcode.com/problems/two-sum/) – Find two numbers in an **unsorted** array.
- [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) – Two sum problem in a **Binary Search Tree**.
