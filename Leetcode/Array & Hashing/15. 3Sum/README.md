# 15. 3Sum

🔗 **[3Sum](https://leetcode.com/problems/3sum/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Two Pointers, Sorting, Array  

---

## Problem Statement

Given an integer array `nums`, return **all** the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, `j != k`
- `nums[i] + nums[j] + nums[k] == 0`
- The solution set **must not contain duplicate triplets**.

---

## Examples

### Example 1:
**Input:**  
```python
nums = [-1,0,1,2,-1,-4]
```
**Output:**  
```python
[[-1,-1,2],[-1,0,1]]
```
**Explanation:**  
- The **distinct** triplets that sum to `0` are `[-1,0,1]` and `[-1,-1,2]`.

### Example 2:
**Input:**  
```python
nums = [0,1,1]
```
**Output:**  
```python
[]
```
**Explanation:**  
There is **no** triplet that sums to `0`.

### Example 3:
**Input:**  
```python
nums = [0,0,0]
```
**Output:**  
```python
[[0,0,0]]
```
**Explanation:**  
The only possible triplet sums up to `0`.

---

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- **We need to find all unique triplets** that sum up to `0` in an **unsorted** array.
- The **order of the triplets does not matter**.
- **Duplicates should be avoided**.
- **Happy Path Test:**  
  Input: `[-1,0,1,2,-1,-4]` → Output: `[[-1,-1,2],[-1,0,1]]`
- **Edge Cases:**  
  - No valid triplets (e.g., `[0,1,1]` → `[]`).
  - All zero triplets (e.g., `[0,0,0]` → `[[0,0,0]]`).
  - Large arrays with `O(N^2)` complexity.

---

### 2️⃣ Match
- **This problem is an extension of the Two Sum II problem.**
- **Problem Category:** Sorting + Two Pointers.
- **Pattern:**  
  - **Sorting**: Sorting helps avoid duplicate triplets.
  - **Two-Pointer Technique**: We use two pointers (`j` and `k`) to efficiently find pairs.

---

### 3️⃣ Plan (Using Two Sum II)
1. **Sort `nums`** (to handle duplicates efficiently).
2. **Iterate Over `nums[i]`**:
   - Treat `nums[i]` as the **fixed first element**.
   - Apply **Two Sum II** to find two numbers that sum to `-nums[i]`.
3. **Apply Two Sum II (`j`, `k`)** – Use two pointers (`j` at `i+1`, `k` at `n-1`):
   - If the sum is **too large**, move `k` left.
   - If the sum is **too small**, move `j` right.
   - If the sum **matches**, store the triplet and skip duplicates.

---

## 4️⃣ Implementation (Python Code)
see sol.py

---

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `[-1,0,1,2,-1,-4]` → Output: `[[-1,-1,2],[-1,0,1]]`
- ✅ **Test with Edge Cases:**  
  - Input: `[0,1,1]` → Output: `[]`  
  - Input: `[0,0,0]` → Output: `[[0,0,0]]`
- ✅ **Checked for Logic Bugs:** Ensured proper two-pointer movement.
- ✅ **Walked through each iteration step-by-step.**

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N^2)`  
  - Sorting takes `O(N log N)`, and the two-pointer search runs in `O(N)`, resulting in an **`O(N^2)` total runtime**.
- **Space Complexity:** `O(1)` (no extra space, result list is output).

**Pros:**  
- **Efficient `O(N^2)` approach** instead of brute force `O(N^3)`.
- **Avoids duplicates using sorting and two-pointer skipping.**

**Cons:**  
- Sorting adds an `O(N log N)` overhead.
- Still `O(N^2)`, but optimal for this problem.

---

### 🔍 How This Solution Uses **Two Sum II**:
- **Sorting helps us reduce duplicate triplets efficiently**.
- Instead of searching for two numbers that sum to `target`, we **search for two numbers that sum to `-nums[i]`**.
- **We apply the Two Sum II technique** to find these pairs efficiently.
- **Example Walkthrough:**  
  ```python
  nums = [-1,0,1,2,-1,-4]
  Step 1: Sort → [-4,-1,-1,0,1,2]
  Step 2: i = -4 → j = -1, k = 2 → sum != 0
  Step 3: i = -1 → j = 0, k = 2 → sum = 1 → move k left
  Step 4: i = -1 → j = 0, k = 1 → sum = 0 → add [-1,0,1]
  ```
- **This ensures unique triplets and an efficient solution**.

---

## 📝 Related Problems
- [1. Two Sum](https://leetcode.com/problems/two-sum/) – Find two numbers in an unsorted array.
- [18. 4Sum](https://leetcode.com/problems/4sum/) – Similar approach with four numbers summing to a target.
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) – **This solution is essentially Two Sum II in a loop!**
