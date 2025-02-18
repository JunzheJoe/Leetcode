# 57. Insert Interval

🔗 **[Insert Interval](https://leetcode.com/problems/insert-interval/)**  
💡 **Difficulty:** Medium  
🛠 **Topics:** Array, Sorting, Interval Merging  

---

## Problem Statement

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

**Note:** You don't need to modify `intervals` in-place. You can make a new array and return it.

---

## Examples

### Example 1:
**Input:**  
```python
intervals = [[1,3],[6,9]], newInterval = [2,5]
```
**Output:**  
```python
[[1,5],[6,9]]
```

### Example 2:
**Input:**  
```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
```
**Output:**  
```python
[[1,2],[3,10],[12,16]]
```
**Explanation:**  
Because the new interval `[4,8]` overlaps with `[3,5],[6,7],[8,10]`.

---

## Constraints
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- We are given a sorted list of non-overlapping intervals.
- Insert a new interval and merge any overlapping intervals.
- **Happy Path Test:**  
  Input: `[[1,3],[6,9]], [2,5]` → Output: `[[1,5],[6,9]]`
- **Edge Cases:**  
  - Empty `intervals` list.
  - `newInterval` that comes before all intervals.
  - `newInterval` that comes after all intervals.
  - `newInterval` that overlaps with multiple intervals.

---

### 2️⃣ Match
- **Problem Category:** Arrays, Interval Merging.
- **Pattern:**  
  - Iterate through the intervals.
  - Merge intervals when there is an overlap.
  - Insert new interval at the correct position.

---

### 3️⃣ Plan
- **Idea:**  
  - Iterate through `intervals`.
  - If `newInterval` ends before the current interval starts, insert `newInterval` and return the result with the remaining intervals.
  - If `newInterval` starts after the current interval ends, add the current interval to the result.
  - Otherwise, merge overlapping intervals by updating the `newInterval` boundaries.
  - After iteration, add the merged `newInterval`.
- **Why This Works:**  
  - The list is sorted, so we can insert at the correct position.
  - Overlapping intervals are merged by updating start/end boundaries.

---

### 4️⃣ Implement
see sol.py

---

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `[[1,3],[6,9]], [2,5]` → Output: `[[1,5],[6,9]]`
- ✅ **Test with Edge Cases:**  
  - Empty intervals → `[]` + `[2,5]` → `[[2,5]]`
  - New interval before all → `[[3,5],[6,7]]` + `[1,2]` → `[[1,2],[3,5],[6,7]]`
  - New interval after all → `[[1,2],[3,5]]` + `[6,7]` → `[[1,2],[3,5],[6,7]]`
  - Overlapping multiple intervals → `[[1,2],[3,5],[6,7],[8,10],[12,16]]` + `[4,8]` → `[[1,2],[3,10],[12,16]]`
- ✅ **Checked for Logic Bugs:** Merging boundaries are calculated correctly.
- ✅ **Walked through each iteration step-by-step.**

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - Single pass through the intervals.
- **Space Complexity:** `O(N)`  
  - Additional array for the result.

**Pros:**  
- Handles all cases efficiently.
- No extra complex data structures needed.

**Cons:**  
- Requires careful boundary handling for merging.

---

### 🔍 Explanation of the Algorithm:
- **Key Insight:**  
  - Non-overlapping intervals are sorted by start times.
  - Iterate and compare `newInterval` with each interval:
    - If `newInterval` ends before the current interval starts, insert it and return.
    - If `newInterval` starts after the current interval ends, add the current interval to `res`.
    - Otherwise, merge by updating `newInterval` with `min` and `max` boundaries.
- **Why This Works:**  
  - The intervals are sorted, allowing for linear iteration.
  - The merge condition ensures no overlaps remain.

---

## 📝 Related Problems
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) – Merge overlapping intervals.
- [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) – Intersection of two interval lists.
