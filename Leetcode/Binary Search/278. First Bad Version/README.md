# 278. First Bad Version

🔗 **[First Bad Version](https://leetcode.com/problems/first-bad-version/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Binary Search  

---

## Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

---

## Examples

### Example 1:
**Input:**  
```python
n = 5, bad = 4
```
**Output:**  
```python
4
```
**Explanation:**  
- call `isBadVersion(3)` → `false`  
- call `isBadVersion(5)` → `true`  
- call `isBadVersion(4)` → `true`  
Then `4` is the first bad version.

### Example 2:
**Input:**  
```python
n = 1, bad = 1
```
**Output:**  
```python
1
```

---

## Constraints
- `1 <= bad <= n <= 2^31 - 1`

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- We need to find the **first bad version** using the `isBadVersion()` API.
- Once a version is marked as bad, all following versions are bad.
- **Happy Path:**  
  Input: `n=5, bad=4` → Output: `4`
- **Edge Cases:**  
  - Minimum `n=1` (e.g., `n=1, bad=1`).
  - Very large `n` (`2^31 - 1`).

---

### 2️⃣ Match
- **Problem Category:** Binary Search.
- **Pattern:**  
  - Apply **binary search** since the array is sorted (good versions first, then bad versions).
  - Minimize API calls → **binary search** reduces calls from `O(n)` to `O(log n)`.

---

### 3️⃣ Plan
- Use **binary search** between `1` and `n`.
- **Pseudocode:**  
  ```
  l = 1, r = n
  while l < r:
      m = (l + r) // 2
      if isBadVersion(m):
          r = m
      else:
          l = m + 1
  return r
  ```
- **Why `while l < r:` and `r = m` instead of `r = m - 1`:**  
  - We use `while l < r` because `l` and `r` should converge exactly at the first bad version.  
  - When `isBadVersion(m)` is `True`, we know the first bad version is at `m` or before it, so we do `r = m` (not `m - 1`), ensuring we **don’t exclude the current version**.  
  - Using `r = m - 1` could skip the actual first bad version.

---

### 4️⃣ Implement
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m    # Include current version if it's bad
            else:
                l = m + 1
        return r
```

---

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `n=5, bad=4` → Output: `4`  
- ✅ **Test with Edge Cases:**  
  - Input: `n=1, bad=1` → Output: `1`  
  - Input: `n=2, bad=1` → Output: `1`  
- ✅ **Check for Logic Bugs:** Ensured boundary conditions are handled.
- ✅ **Walked through each step of binary search** to confirm correctness.

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(log n)`  
  - Binary search halves the search space each iteration.
- **Space Complexity:** `O(1)`  
  - Uses only a few variables, no additional data structures.

**Pros:**  
- Efficient for large `n` values.  
- Minimal API calls due to binary search.

**Cons:**  
- Requires careful handling of boundaries (`l`, `r`, and `m`).

---

## 📝 Related Problems
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)  
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
