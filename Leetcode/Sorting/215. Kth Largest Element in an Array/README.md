# 215. Kth Largest Element in an Array

🔗 **[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Quickselect, Heap, Sorting, Divide & Conquer  

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the **k-th largest element in the array**.

- The **k-th largest element** means the **k-th element when sorted in descending order**.
- **Note:** This is **not the k-th distinct element**.

**Can you solve it without sorting?**

---

## Examples

### Example 1:
**Input:**  
```python
nums = [3,2,1,5,6,4]
k = 2
```
**Output:**  
```python
5
```
**Explanation:**  
- The sorted array is `[6, 5, 4, 3, 2, 1]`, and the **2nd largest** element is `5`.

### Example 2:
**Input:**  
```python
nums = [3,2,3,1,2,4,5,5,6]
k = 4
```
**Output:**  
```python
4
```
**Explanation:**  
- The sorted array is `[6, 5, 5, 4, 3, 3, 2, 2, 1]`, and the **4th largest** element is `4`.

---

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. **What does "k-th largest" mean?**  
   - The k-th element **when sorted in descending order**.
2. **Can we use sorting?**  
   - Yes, but it has **O(N log N) time complexity**.
3. **Can we solve it more efficiently?**  
   - Yes, using **Quickselect (O(N) average case)** or **Min-Heap (O(N log K))**.

### 2️⃣ Match
- **Sorting Approach:** `O(N log N)` using `sort()`.
- **Heap Approach:** `O(N log K)`, maintaining a Min-Heap of size `k`.
- **Quickselect Approach:** **O(N) average-case**, **O(N^2) worst-case**.

### 3️⃣ Plan (Quickselect Approach)
1. Use **Quickselect**, a modified **Quicksort**.
2. Choose a **pivot** (last element in the range).
3. **Partition** the array such that:
   - Elements **≤ pivot** are on the left.
   - Elements **> pivot** are on the right.
4. Recursively **search in the correct partition**:
   - If `pivot index > k`, search the **left** partition.
   - If `pivot index < k`, search the **right** partition.
   - Else, return `nums[pivot index]`.

---

## 4️⃣ Implementation (Quickselect Approach)
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the length of `nums`.

- **Sorting Approach:**  
  - **Time Complexity:** `O(N log N)`  
  - **Space Complexity:** `O(1)`

- **Heap Approach (Min-Heap of size `k`)**  
  - **Time Complexity:** `O(N log K)`  
  - **Space Complexity:** `O(K)`

- **Quickselect Approach (Used Above)**  
  - **Time Complexity:** `O(N)` (average), `O(N^2)` (worst-case)  
  - **Space Complexity:** `O(1)`

---

## 6️⃣ Additional Notes
- **Quickselect is best for large `N`** when `O(N log N)` sorting is too slow.
- **Min-Heap is preferred** when `k` is small (`k << N`).
- **Sorting is simplest** but inefficient for large inputs.

---

## 📝 Related Problems
- [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
