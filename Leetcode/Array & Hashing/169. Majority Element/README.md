# 169. Majority Element

🔗 **[Majority Element](https://leetcode.com/problems/majority-element/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Array, Hash Table, Divide and Conquer, Sorting, Boyer-Moore Voting Algorithm  

---

## Problem Statement

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears more than `n / 2` times. You may assume that the majority element always exists in the array.

---

## Examples

### Example 1:
**Input:**  
```python
nums = [3,2,3]
```
**Output:**  
```python
3
```

### Example 2:
**Input:**  
```python
nums = [2,2,1,1,1,2,2]
```
**Output:**  
```python
2
```

---

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- We need to find the **majority element** in an array.
- A majority element appears more than `n/2` times.
- **Happy Path Test:**  
  Input: `[3,2,3]` → Output: `3`  
- **Edge Cases:**  
  - Single-element array (e.g., `[1]` → Output: `1`).
  - All elements are the same (e.g., `[2,2,2,2]` → Output: `2`).

---

### 2️⃣ Match
- **Problem Category:** Arrays, Counting.
- **Pattern:**  
  - **Boyer-Moore Voting Algorithm**: A well-known algorithm to find the majority element in `O(N)` time and `O(1)` space.
  - Uses a counter that increments when the candidate element is seen and decrements for other elements.

---

### 3️⃣ Plan
- **Idea:**  
  - Initialize `res` as 0 and `count` as 0.
  - Iterate through `nums`:
    - If `count == 0`, set `res = num`.
    - Increment `count` if `num == res`, otherwise decrement.
  - Return `res` at the end.
- **Why Boyer-Moore?**  
  - **Linear time (O(N))**: Iterates once through the array.
  - **Constant space (O(1))**: Uses only two variables.

---

### 4️⃣ Implement
see sol.py

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `[2,2,1,1,1,2,2]` → Output: `2`  
- ✅ **Test with Edge Cases:**  
  - Input: `[1]` → Output: `1`  
  - Input: `[5,5,5,5]` → Output: `5`  
- ✅ **Check for Logic Bugs:** Counter increments/decrements correctly.
- ✅ **Debug Steps:** Walked through each iteration with multiple test cases.

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - Single pass through the array.
- **Space Complexity:** `O(1)`  
  - Uses two variables (`res` and `count`).

**Pros:**  
- Optimal for large datasets due to `O(N)` time and `O(1)` space.
- Simple implementation with no additional data structures.

**Cons:**  
- Assumes a majority element always exists.

---

### 🔍 Why Boyer-Moore Voting Algorithm Works:
- **Concept:**  
  - Imagine you are "voting" for candidates.  
  - Every time you encounter the same candidate, you add a vote.  
  - Every time you encounter a different candidate, you subtract a vote.  
- **Why it works:**  
  - The majority element **always outnumbers the rest combined**.  
  - Even after all cancellations, the majority element remains.  
  - By the end, the candidate with the most votes is the majority.
- **Example:**  
  Array: `[2,2,1,1,1,2,2]`  
  Steps:  
  - `count=0`, choose `2` as `res` → `count=1`  
  - Next `2` → `count=2`  
  - Next `1` → `count=1`  
  - Next `1` → `count=0` (cancelled out equal votes)  
  - Next `1` → `res=1`, `count=1`  
  - Next `2` → `count=0`  
  - Next `2` → `res=2`, `count=1`  
  - Final: Majority is `2`.

---

## 📝 Related Problems
- [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) – Find elements appearing more than `n/3` times.  
- [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/) – Another array problem with optimization techniques.
