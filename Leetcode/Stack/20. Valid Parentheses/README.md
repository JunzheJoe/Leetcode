# 1. Two Sum

🔗 **[Two Sum](https://leetcode.com/problems/two-sum/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Array & Hashing

---

### Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

- Each input has **exactly one solution**.
- **You may not use the same element twice**.
- You can return the answer **in any order**.

---

### Examples

#### Example 1:
**Input:**  
`nums = [2,7,11,15], target = 9`  
**Output:** `[0,1]`  
**Explanation:** `nums[0] + nums[1] == 9`, so we return `[0, 1]`.

#### Example 2:
**Input:**  
`nums = [3,2,4], target = 6`  
**Output:** `[1,2]`  

#### Example 3:
**Input:**  
`nums = [3,3], target = 6`  
**Output:** `[0,1]`  

---

### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. Can the nums array be empty?
2. Any requirement on time/space complexity?
3. Is the array sorted?
4. Will the numbers in the array duplicate?

### 2️⃣ Match
Using a hashmap to store the elements of the array enables us to efficiently maintain the association between indices and values, where each value is paired with its corresponding index (key: value)

### 3️⃣ Plan
General Idea: Create a hashmap to store index and number so that we can refer to the hashmap for the index once we find the counterpart.

1) Create a hashmap that store the previous numbers
2) Iterate through the array
    - Calculate the diff (target - current number)
    - If we see the diff exists in our hashmap then return the [index of the diff, current index]
    - Else store the current number and the current index into the hashmap
    - We are guaranteed to have exactly one solution

---

### 4️⃣ Implementation

📌 **See `sol.py` for the code.**

---

### 5️⃣ Complexity Analysis
Assume `N` is the length of the input array:

- **Brute Force Approach:**  
  - Time Complexity: `O(N^2)`  
  - Space Complexity: `O(1)`

- **Optimized Approach (Using Hash Table):**  
  - Time Complexity: `O(N)`  
  - Space Complexity: `O(N)`

---

### 6️⃣ Additional Notes
- This problem is a classic example of using **hash tables** to improve efficiency.
- The brute force approach works but is inefficient for large inputs.

---

### 📝 Related Problems
- [167. Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
